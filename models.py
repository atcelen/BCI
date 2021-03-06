#*----------------------------------------------------------------------------*
#* Copyright (C) 2020 ETH Zurich, Switzerland                                 *
#* SPDX-License-Identifier: Apache-2.0                                        *
#*                                                                            *
#* Licensed under the Apache License, Version 2.0 (the "License");            *
#* you may not use this file except in compliance with the License.           *
#* You may obtain a copy of the License at                                    *
#*                                                                            *
#* http://www.apache.org/licenses/LICENSE-2.0                                 *
#*                                                                            *
#* Unless required by applicable law or agreed to in writing, software        *
#* distributed under the License is distributed on an "AS IS" BASIS,          *
#* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   *
#* See the License for the specific language governing permissions and        *
#* limitations under the License.                                             *
#*                                                                            *
#* Authors: Batuhan Toemekce, Burak Kaya, Michael Hersche                     *
#*----------------------------------------------------------------------------*


from keras.models import Model
from keras.layers.core import Dense, Activation
from keras.layers.convolutional import Conv2D, AveragePooling2D
from keras.layers.convolutional import SeparableConv2D
from keras.layers.normalization import BatchNormalization
from keras.layers import SpatialDropout2D, Dropout
from keras.regularizers import l1_l2
from keras.layers import Input, Flatten
from keras.layers import DepthwiseConv2D
from tensorflow.keras.constraints import max_norm


###################################################################
############## EEGnet model changed from loaded model #############
###################################################################

def EEGNet(nb_classes, Chans=64, Samples=128, regRate=.25,
			   dropoutRate=0.1, kernLength=128,poolLength=8, 
			   numFilters=8, dropoutType='Dropout'):
	"""
	Inputs:

		nb_classes: int, number of classes to classify
		Chans, Samples: number of channels and time points in the EEG data
		regRate: regularization parameter for L1 and L2 penalties
		dropoutRate: dropout fraction
		kernLength: length of temporal convolution in first layer
		numFilters: number of temporal-spatial filter pairs to learn

	Depending on the task, using numFilters = 4 or 8 seemed to do pretty well
	across tasks.

	"""
	F1 = numFilters
	D = 2
	F2= numFilters*2
	if dropoutType == 'SpatialDropout2D':
		dropoutType = SpatialDropout2D
	elif dropoutType == 'Dropout':
		dropoutType = Dropout
	else:
		raise ValueError('dropoutType must be one of SpatialDropout2D '
						 'or Dropout, passed as a string.')
	
	input1   = Input(shape = (Chans, Samples,1))

	##################################################################
	block1       = Conv2D(F1, (1, kernLength), padding = 'same',
								   input_shape = (Chans, Samples,1),
								   use_bias = False)(input1)
	block1       = BatchNormalization(axis = 1)(block1)
	block1       = DepthwiseConv2D((Chans, 1), use_bias = False, 
								   depth_multiplier = D,
								   depthwise_constraint = max_norm(1.))(block1)
	block1       = BatchNormalization(axis = 1)(block1)
	block1       = Activation('relu')(block1)
	block1       = AveragePooling2D((1, poolLength))(block1) # changed from 4 to 8
	block1       = dropoutType(dropoutRate)(block1)
	
	# block2       = SeparableConv2D(F2, (1, 16),
	# 				use_bias = False, padding = 'same')(block1)
	# block2       = BatchNormalization(axis = 1)(block2)
	# block2       = Activation('relu')(block2)
	# block2       = AveragePooling2D((1, 8))(block2)
	# block2       = dropoutType(dropoutRate)(block2)
		
	flatten      = Flatten(name = 'flatten')(block1)
	
	dense        = Dense(nb_classes, name = 'dense', 
						 kernel_constraint = max_norm(regRate))(flatten)
	softmax      = Activation('softmax', name = 'softmax')(dense)
	
	return Model(inputs=input1, outputs=softmax)


