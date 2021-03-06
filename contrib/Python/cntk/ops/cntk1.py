# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root 
# for full license information.
# ==============================================================================

# This file is auto-generated by _fetch_ops.py.

from cntk.graph import ComputationNode, _InputComputationNodeBase, _ImageInputComputationNodeBase

class Slice(ComputationNode):
    def __init__(self, beginIndex, endIndex, input, axis=1, op_name='Slice',
            name=None):
        super(Slice, self).__init__(params=['beginIndex', 'endIndex', 'input', 'axis'], op_name=op_name, name=name)
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.input = input
        self.axis = axis
        self.inputs = ['input']
        self.params_with_defaults = []

class Splice(ComputationNode):
    def __init__(self, beginIndex, endIndex, input, axis=1, op_name='Splice',
            name=None):
        super(Splice, self).__init__(params=['beginIndex', 'endIndex', 'input', 'axis'], op_name=op_name, name=name)
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.input = input
        self.axis = axis
        self.inputs = ['input']
        self.params_with_defaults = []
    
class ElementDivide(ComputationNode):
    def __init__(self, aMatrix, anotherMatrix, op_name='ElementDivide', name=None):
        super(ElementDivide, self).__init__(params=['aMatrix', 'anotherMatrix'], op_name=op_name, name=name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix
        self.inputs = ['aMatrix', 'anotherMatrix']
        self.params_with_defaults = []
        
class Round(ComputationNode):
    def __init__(self, x, op_name='Round', name=None):
        super(Round, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.inputs = ['x']
        self.params_with_defaults = []
        
class Ceil(ComputationNode):
    def __init__(self, x, op_name='Ceil', name=None):
        super(Ceil, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.inputs = ['x']
        self.params_with_defaults = []

class If(ComputationNode):
    def __init__(self, cond, thenVal, elseVal, op_name='BS.Boolean.If', name=None):
        super(If, self).__init__(
            params=['cond', 'thenVal', 'elseVal'], op_name=op_name, name=name)
        self.cond = cond
        self.thenVal = thenVal
        self.elseVal = elseVal
        self.params_with_defaults = []
        self.inputs = ['cond', 'thenVal', 'elseVal']

class Sign(ComputationNode):
    def __init__(self, x, op_name='Sign', name=None):
        super(Sign, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.params_with_defaults = []
        self.inputs = []

class Min(ComputationNode):
    def __init__(self, a, b, op_name='Min', name=None):
        super(Min, self).__init__(params=['a', 'b'], op_name=op_name, name=name)
        self.a = a
        self.b = b
        self.params_with_defaults = []
        self.inputs = []

class Max(ComputationNode):
    def __init__(self, a, b, op_name='Max', name=None):
        super(Max, self).__init__(params=['a', 'b'], op_name=op_name, name=name)
        self.a = a
        self.b = b
        self.params_with_defaults = []
        self.inputs = []

class Fac(ComputationNode):
    def __init__(self, n, op_name='Fac', name=None):
        super(Fac, self).__init__(params=['n'], op_name=op_name, name=name)
        self.n = n
        self.params_with_defaults = []
        self.inputs = []

class IsSameObject(ComputationNode):
    def __init__(self, a, b, op_name='IsSameObject', name=None):
        super(IsSameObject, self).__init__(params=['a', 'b'], op_name=op_name, name=name)
        self.a = a
        self.b = b
        self.params_with_defaults = []
        self.inputs = []

class LearnableParameter(ComputationNode):
    def __init__(self, outputDim, inputDim, learningRateMultiplier=1.0, init='uniform', initValueScale=1, value=0, initFromFilePath='', initFromLiteral='', initOnCPUOnly=True, randomSeed=-1, op_name='LearnableParameter', name=None):
        super(LearnableParameter, self).__init__(params=['outputDim', 'inputDim', 'learningRateMultiplier', 'init', 'initValueScale', 'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed'], op_name=op_name, name=name)
        self.outputDim = outputDim
        self.inputDim = inputDim
        self.learningRateMultiplier = learningRateMultiplier
        self.init = init
        self.initValueScale = initValueScale
        self.value = value
        self.initFromFilePath = initFromFilePath
        self.initFromLiteral = initFromLiteral
        self.initOnCPUOnly = initOnCPUOnly
        self.randomSeed = randomSeed
        self.params_with_defaults = ['learningRateMultiplier', 'init', 'initValueScale', 'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed']
        self.inputs = []

class ParameterTensor(ComputationNode):
    def __init__(self, dims, learningRateMultiplier=1.0, init='uniform', initValueScale=1, value=0, initFromFilePath='', initFromLiteral='', initOnCPUOnly=True, randomSeed=-1, op_name='ParameterTensor', name=None):
        super(ParameterTensor, self).__init__(params=['dims', 'learningRateMultiplier', 'init', 'initValueScale', 'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed'], op_name=op_name, name=name)
        self.dims = dims
        self.learningRateMultiplier = learningRateMultiplier
        self.init = init
        self.initValueScale = initValueScale
        self.value = value
        self.initFromFilePath = initFromFilePath
        self.initFromLiteral = initFromLiteral
        self.initOnCPUOnly = initOnCPUOnly
        self.randomSeed = randomSeed
        self.params_with_defaults = ['learningRateMultiplier', 'init', 'initValueScale', 'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed']
        self.inputs = []

class DynamicAxis(ComputationNode):
    def __init__(self, op_name='DynamicAxis', name=None):
        super(DynamicAxis, self).__init__(params=[], op_name=op_name, name=name)

        self.params_with_defaults = []
        self.inputs = []

class Input(_InputComputationNodeBase):
    def __init__(self, dims, dynamicAxis='', tag='feature', op_name='Input', name=None):
        super(Input, self).__init__(params=['dims', 'dynamicAxis', 'tag'], op_name=op_name, name=name)
        self.dims = dims
        self.dynamicAxis = dynamicAxis
        self.tag = tag
        self.params_with_defaults = ['dynamicAxis', 'tag']
        self.inputs = []

class SparseInput(_InputComputationNodeBase):
    def __init__(self, dims, dynamicAxis='', tag='feature', op_name='SparseInput', name=None):
        super(SparseInput, self).__init__(params=['dims', 'dynamicAxis', 'tag'], op_name=op_name, name=name)
        self.dims = dims
        self.dynamicAxis = dynamicAxis
        self.tag = tag
        self.params_with_defaults = ['dynamicAxis', 'tag']
        self.inputs = []

class ImageInput(_ImageInputComputationNodeBase):
    def __init__(self, imageWidth, imageHeight, imageChannels, imageLayout='CHW', dynamicAxis='', tag='feature', op_name='ImageInput', name=None):
        super(ImageInput, self).__init__(params=['imageWidth', 'imageHeight', 'imageChannels', 'imageLayout', 'dynamicAxis', 'tag'], op_name=op_name, name=name)
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.imageLayout = imageLayout
        self.dynamicAxis = dynamicAxis
        self.tag = tag
        self.params_with_defaults = ['imageLayout', 'dynamicAxis', 'tag']
        self.inputs = []

class SparseImageInput(_ImageInputComputationNodeBase):
    def __init__(self, imageWidth, imageHeight, imageChannels, imageLayout='CHW', dynamicAxis='', tag='feature', op_name='SparseImageInput', name=None):
        super(SparseImageInput, self).__init__(params=['imageWidth', 'imageHeight', 'imageChannels', 'imageLayout', 'dynamicAxis', 'tag'], op_name=op_name, name=name)
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.imageLayout = imageLayout
        self.dynamicAxis = dynamicAxis
        self.tag = tag
        self.params_with_defaults = ['imageLayout', 'dynamicAxis', 'tag']
        self.inputs = []

class EnvironmentInput(ComputationNode):
    def __init__(self, propertyName, op_name='EnvironmentInput', name=None):
        super(EnvironmentInput, self).__init__(params=['propertyName'], op_name=op_name, name=name)
        self.propertyName = propertyName
        self.params_with_defaults = []
        self.inputs = []

class PastValue(ComputationNode):
    def __init__(self, dims, input, timeStep=1, defaultHiddenActivation=0.1, op_name='PastValue', name=None):
        super(PastValue, self).__init__(params=['dims', 'input', 'timeStep', 'defaultHiddenActivation'], op_name=op_name, name=name)
        self.dims = dims
        self.input = input
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation
        self.params_with_defaults = ['timeStep', 'defaultHiddenActivation']
        self.inputs = ['input']

class FutureValue(ComputationNode):
    def __init__(self, dims, input, timeStep=1, defaultHiddenActivation=0.1, op_name='FutureValue', name=None):
        super(FutureValue, self).__init__(params=['dims', 'input', 'timeStep', 'defaultHiddenActivation'], op_name=op_name, name=name)
        self.dims = dims
        self.input = input
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation
        self.params_with_defaults = ['timeStep', 'defaultHiddenActivation']
        self.inputs = ['input']

class Shift(ComputationNode):
    def __init__(self, input, fromOffset, boundaryValue, boundaryMode=-1, dim=-1, op_name='Shift', name=None):
        super(Shift, self).__init__(params=['input', 'fromOffset', 'boundaryValue', 'boundaryMode', 'dim'], op_name=op_name, name=name)
        self.input = input
        self.fromOffset = fromOffset
        self.boundaryValue = boundaryValue
        self.boundaryMode = boundaryMode
        self.dim = dim
        self.params_with_defaults = ['boundaryMode', 'dim']
        self.inputs = ['input', 'boundaryValue']

class RowRepeat(ComputationNode):
    def __init__(self, input, numRepeats, op_name='RowRepeat', name=None):
        super(RowRepeat, self).__init__(params=['input', 'numRepeats'], op_name=op_name, name=name)
        self.input = input
        self.numRepeats = numRepeats
        self.params_with_defaults = []
        self.inputs = ['input']

class RowStack(ComputationNode):
    def __init__(self, inputs, op_name='RowStack', name=None):
        super(RowStack, self).__init__(params=['inputs'], op_name=op_name, name=name)
        self.inputs = inputs
        self.params_with_defaults = []
        self.inputs = []

class Reshape(ComputationNode):
    def __init__(self, input, numRows, imageWidth=0, imageHeight=0, imageChannels=0, op_name='Reshape', name=None):
        super(Reshape, self).__init__(params=['input', 'numRows', 'imageWidth', 'imageHeight', 'imageChannels'], op_name=op_name, name=name)
        self.input = input
        self.numRows = numRows
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.params_with_defaults = ['imageWidth', 'imageHeight', 'imageChannels']
        self.inputs = ['input']

class NewReshape(ComputationNode):
    def __init__(self, input, dims, beginAxis=0, endAxis=0, op_name='NewReshape', name=None):
        super(NewReshape, self).__init__(params=['input', 'dims', 'beginAxis', 'endAxis'], op_name=op_name, name=name)
        self.input = input
        self.dims = dims
        self.beginAxis = beginAxis
        self.endAxis = endAxis
        self.params_with_defaults = ['beginAxis', 'endAxis']
        self.inputs = ['input']

class TransposeDimensions(ComputationNode):
    def __init__(self, input, axis1, axis2, op_name='TransposeDimensions', name=None):
        super(TransposeDimensions, self).__init__(params=['input', 'axis1', 'axis2'], op_name=op_name, name=name)
        self.input = input
        self.axis1 = axis1
        self.axis2 = axis2
        self.params_with_defaults = []
        self.inputs = ['input']

class Times(ComputationNode):
    def __init__(self, A, B, outputRank=1, op_name='Times', name=None):
        super(Times, self).__init__(params=['A', 'B', 'outputRank'], op_name=op_name, name=name)
        self.A = A
        self.B = B
        self.outputRank = outputRank
        self.params_with_defaults = ['outputRank']
        self.inputs = ['A', 'B']

class Logistic(ComputationNode):
    def __init__(self, label, probability, op_name='Logistic', name=None):
        super(Logistic, self).__init__(params=['label', 'probability'], op_name=op_name, name=name)
        self.label = label
        self.probability = probability
        self.params_with_defaults = []
        self.inputs = ['label', 'probability']

class WeightedLogistic(ComputationNode):
    def __init__(self, label, probability, instanceWeight, op_name='WeightedLogistic', name=None):
        super(WeightedLogistic, self).__init__(params=['label', 'probability', 'instanceWeight'], op_name=op_name, name=name)
        self.label = label
        self.probability = probability
        self.instanceWeight = instanceWeight
        self.params_with_defaults = []
        self.inputs = ['label', 'probability', 'instanceWeight']

class ReconcileDynamicAxis(ComputationNode):
    def __init__(self, dataInput, layoutInput, op_name='ReconcileDynamicAxis', name=None):
        super(ReconcileDynamicAxis, self).__init__(params=['dataInput', 'layoutInput'], op_name=op_name, name=name)
        self.dataInput = dataInput
        self.layoutInput = layoutInput
        self.params_with_defaults = []
        self.inputs = ['dataInput', 'layoutInput']

class Convolution(ComputationNode):
    def __init__(self, weightNode, inputValueNode, kernelDims, mapDims=1, stride=1, sharing=True, autoPadding=True, lowerPad=0, upperPad=0, imageLayout='CHW', maxTempMemSizeInSamples=0, op_name='Convolution', name=None):
        super(Convolution, self).__init__(params=['weightNode', 'inputValueNode', 'kernelDims', 'mapDims', 'stride', 'sharing', 'autoPadding', 'lowerPad', 'upperPad', 'imageLayout', 'maxTempMemSizeInSamples'], op_name=op_name, name=name)
        self.weightNode = weightNode
        self.inputValueNode = inputValueNode
        self.kernelDims = kernelDims
        self.mapDims = mapDims
        self.stride = stride
        self.sharing = sharing
        self.autoPadding = autoPadding
        self.lowerPad = lowerPad
        self.upperPad = upperPad
        self.imageLayout = imageLayout
        self.maxTempMemSizeInSamples = maxTempMemSizeInSamples
        self.params_with_defaults = ['mapDims', 'stride', 'sharing', 'autoPadding', 'lowerPad', 'upperPad', 'imageLayout', 'maxTempMemSizeInSamples']
        self.inputs = ['weightNode', 'inputValueNode']

class Pooling(ComputationNode):
    def __init__(self, input, poolKind, kernelDims, stride=1, autoPadding=True, lowerPad=0, upperPad=0, imageLayout='CHW', op_name='Pooling', name=None):
        super(Pooling, self).__init__(params=['input', 'poolKind', 'kernelDims', 'stride', 'autoPadding', 'lowerPad', 'upperPad', 'imageLayout'], op_name=op_name, name=name)
        self.input = input
        self.poolKind = poolKind
        self.kernelDims = kernelDims
        self.stride = stride
        self.autoPadding = autoPadding
        self.lowerPad = lowerPad
        self.upperPad = upperPad
        self.imageLayout = imageLayout
        self.params_with_defaults = ['stride', 'autoPadding', 'lowerPad', 'upperPad', 'imageLayout']
        self.inputs = ['input']

class MaxPooling(ComputationNode):
    def __init__(self, input, windowWidth, windowHeight, horizontalSubsample, verticalSubsample, imageLayout='CHW', op_name='MaxPooling', name=None):
        super(MaxPooling, self).__init__(params=['input', 'windowWidth', 'windowHeight', 'horizontalSubsample', 'verticalSubsample', 'imageLayout'], op_name=op_name, name=name)
        self.input = input
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.horizontalSubsample = horizontalSubsample
        self.verticalSubsample = verticalSubsample
        self.imageLayout = imageLayout
        self.params_with_defaults = ['imageLayout']
        self.inputs = ['input']

class AveragePooling(ComputationNode):
    def __init__(self, input, windowWidth, windowHeight, horizontalSubsample, verticalSubsample, imageLayout='CHW', op_name='AveragePooling', name=None):
        super(AveragePooling, self).__init__(params=['input', 'windowWidth', 'windowHeight', 'horizontalSubsample', 'verticalSubsample', 'imageLayout'], op_name=op_name, name=name)
        self.input = input
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.horizontalSubsample = horizontalSubsample
        self.verticalSubsample = verticalSubsample
        self.imageLayout = imageLayout
        self.params_with_defaults = ['imageLayout']
        self.inputs = ['input']

class BatchNormalization(ComputationNode):
    def __init__(self, input, scale, bias, runMean, runInvStdDev, spatial, normalizationTimeConstant=0, blendTimeConstant=0, epsilon=1e-05, useCntkEngine=True, imageLayout='CHW', op_name='BatchNormalization', name=None):
        super(BatchNormalization, self).__init__(params=['input', 'scale', 'bias', 'runMean', 'runInvStdDev', 'spatial', 'normalizationTimeConstant', 'blendTimeConstant', 'epsilon', 'useCntkEngine', 'imageLayout'], op_name=op_name, name=name)
        self.input = input
        self.scale = scale
        self.bias = bias
        self.runMean = runMean
        self.runInvStdDev = runInvStdDev
        self.spatial = spatial
        self.normalizationTimeConstant = normalizationTimeConstant
        self.blendTimeConstant = blendTimeConstant
        self.epsilon = epsilon
        self.useCntkEngine = useCntkEngine
        self.imageLayout = imageLayout
        self.params_with_defaults = ['normalizationTimeConstant', 'blendTimeConstant', 'epsilon', 'useCntkEngine', 'imageLayout']
        self.inputs = ['input', 'scale', 'bias', 'runMean', 'runInvStdDev']

class Abs(ComputationNode):
    def __init__(self, x, op_name='Abs', name=None):
        super(Abs, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.params_with_defaults = []
        self.inputs = ['x']

class ClassBasedCrossEntropyWithSoftmax(ComputationNode):
    def __init__(self, labelClassDescriptorVectorSequence, mainInputInfo, mainWeight, classLogProbsBeforeSoftmax, op_name='ClassBasedCrossEntropyWithSoftmax', name=None):
        super(ClassBasedCrossEntropyWithSoftmax, self).__init__(params=['labelClassDescriptorVectorSequence', 'mainInputInfo', 'mainWeight', 'classLogProbsBeforeSoftmax'], op_name=op_name, name=name)
        self.labelClassDescriptorVectorSequence = labelClassDescriptorVectorSequence
        self.mainInputInfo = mainInputInfo
        self.mainWeight = mainWeight
        self.classLogProbsBeforeSoftmax = classLogProbsBeforeSoftmax
        self.params_with_defaults = []
        self.inputs = ['labelClassDescriptorVectorSequence', 'mainInputInfo', 'mainWeight', 'classLogProbsBeforeSoftmax']

class Clip(ComputationNode):
    def __init__(self, minValue, maxValue, x, op_name='Clip', name=None):
        super(Clip, self).__init__(params=['minValue', 'maxValue', 'x'], op_name=op_name, name=name)
        self.minValue = minValue
        self.maxValue = maxValue
        self.x = x
        self.params_with_defaults = []
        self.inputs = ['minValue', 'maxValue', 'x']

class ColumnElementTimes(ComputationNode):
    def __init__(self, aVectorSequence, anotherVectorSequence, op_name='ColumnElementTimes', name=None):
        super(ColumnElementTimes, self).__init__(params=['aVectorSequence', 'anotherVectorSequence'], op_name=op_name, name=name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence
        self.params_with_defaults = []
        self.inputs = ['aVectorSequence', 'anotherVectorSequence']

class CosDistance(ComputationNode):
    def __init__(self, aVectorSequence, anotherVectorSequence, op_name='CosDistance', name=None):
        super(CosDistance, self).__init__(params=['aVectorSequence', 'anotherVectorSequence'], op_name=op_name, name=name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence
        self.params_with_defaults = []
        self.inputs = ['aVectorSequence', 'anotherVectorSequence']

class CosDistanceWithNegativeSamples(ComputationNode):
    def __init__(self, aVectorSequence, anotherVectorSequence, numShifts, numNegSamples, op_name='CosDistanceWithNegativeSamples', name=None):
        super(CosDistanceWithNegativeSamples, self).__init__(params=['aVectorSequence', 'anotherVectorSequence', 'numShifts', 'numNegSamples'], op_name=op_name, name=name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence
        self.numShifts = numShifts
        self.numNegSamples = numNegSamples
        self.params_with_defaults = []
        self.inputs = ['aVectorSequence', 'anotherVectorSequence', 'numShifts', 'numNegSamples']

class Cosine(ComputationNode):
    def __init__(self, x, op_name='Cosine', name=None):
        super(Cosine, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.params_with_defaults = []
        self.inputs = ['x']

class CrossEntropy(ComputationNode):
    def __init__(self, refProbVectorSequence, outProbVectorSequence, op_name='CrossEntropy', name=None):
        super(CrossEntropy, self).__init__(params=['refProbVectorSequence', 'outProbVectorSequence'], op_name=op_name, name=name)
        self.refProbVectorSequence = refProbVectorSequence
        self.outProbVectorSequence = outProbVectorSequence
        self.params_with_defaults = []
        self.inputs = ['refProbVectorSequence', 'outProbVectorSequence']

class CrossEntropyWithSoftmax(ComputationNode):
    def __init__(self, labelVectorSequence, outProbVectorSequence, op_name='CrossEntropyWithSoftmax', name=None):
        super(CrossEntropyWithSoftmax, self).__init__(params=['labelVectorSequence', 'outProbVectorSequence'], op_name=op_name, name=name)
        self.labelVectorSequence = labelVectorSequence
        self.outProbVectorSequence = outProbVectorSequence
        self.params_with_defaults = []
        self.inputs = ['labelVectorSequence', 'outProbVectorSequence']

class DiagTimes(ComputationNode):
    def __init__(self, diagonalMatrixAsColumnVector, matrix, op_name='DiagTimes', name=None):
        super(DiagTimes, self).__init__(params=['diagonalMatrixAsColumnVector', 'matrix'], op_name=op_name, name=name)
        self.diagonalMatrixAsColumnVector = diagonalMatrixAsColumnVector
        self.matrix = matrix
        self.params_with_defaults = []
        self.inputs = ['diagonalMatrixAsColumnVector', 'matrix']

class Dropout(ComputationNode):
    def __init__(self, activationVectorSequence, op_name='Dropout', name=None):
        super(Dropout, self).__init__(params=['activationVectorSequence'], op_name=op_name, name=name)
        self.activationVectorSequence = activationVectorSequence
        self.params_with_defaults = []
        self.inputs = ['activationVectorSequence']

class ElementTimes(ComputationNode):
    def __init__(self, aMatrix, anotherMatrix, op_name='ElementTimes', name=None):
        super(ElementTimes, self).__init__(params=['aMatrix', 'anotherMatrix'], op_name=op_name, name=name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix
        self.params_with_defaults = []
        self.inputs = ['aMatrix', 'anotherMatrix']

class ErrorPrediction(ComputationNode):
    def __init__(self, labelVectorSequence, outVectorSequence, op_name='ErrorPrediction', name=None):
        super(ErrorPrediction, self).__init__(params=['labelVectorSequence', 'outVectorSequence'], op_name=op_name, name=name)
        self.labelVectorSequence = labelVectorSequence
        self.outVectorSequence = outVectorSequence
        self.params_with_defaults = []
        self.inputs = ['labelVectorSequence', 'outVectorSequence']

class Exp(ComputationNode):
    def __init__(self, x, op_name='Exp', name=None):
        super(Exp, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.params_with_defaults = []
        self.inputs = ['x']

class Floor(ComputationNode):
    def __init__(self, x, op_name='Floor', name=None):
        super(Floor, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.params_with_defaults = []
        self.inputs = ['x']

class GatherPacked(ComputationNode):
    def __init__(self, indexSequence, sourceData, op_name='GatherPacked', name=None):
        super(GatherPacked, self).__init__(params=['indexSequence', 'sourceData'], op_name=op_name, name=name)
        self.indexSequence = indexSequence
        self.sourceData = sourceData
        self.params_with_defaults = []
        self.inputs = ['indexSequence', 'sourceData']

class GMMLogLikelihood(ComputationNode):
    def __init__(self, unnormalizedPriorVector, meansAsRows, logStdDevAsRows, dataVectorSequence, op_name='GMMLogLikelihood', name=None):
        super(GMMLogLikelihood, self).__init__(params=['unnormalizedPriorVector', 'meansAsRows', 'logStdDevAsRows', 'dataVectorSequence'], op_name=op_name, name=name)
        self.unnormalizedPriorVector = unnormalizedPriorVector
        self.meansAsRows = meansAsRows
        self.logStdDevAsRows = logStdDevAsRows
        self.dataVectorSequence = dataVectorSequence
        self.params_with_defaults = []
        self.inputs = ['unnormalizedPriorVector', 'meansAsRows', 'logStdDevAsRows', 'dataVectorSequence']

class InvStdDev(ComputationNode):
    def __init__(self, dataVectorSequence, op_name='InvStdDev', name=None):
        super(InvStdDev, self).__init__(params=['dataVectorSequence'], op_name=op_name, name=name)
        self.dataVectorSequence = dataVectorSequence
        self.params_with_defaults = []
        self.inputs = ['dataVectorSequence']

class KhatriRaoProduct(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, op_name='KhatriRaoProduct', name=None):
        super(KhatriRaoProduct, self).__init__(params=['leftMatrix', 'rightMatrix'], op_name=op_name, name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []
        self.inputs = ['leftMatrix', 'rightMatrix']

class Log(ComputationNode):
    def __init__(self, x, op_name='Log', name=None):
        super(Log, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.params_with_defaults = []
        self.inputs = ['x']

class LogPlus(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, op_name='LogPlus', name=None):
        super(LogPlus, self).__init__(params=['leftMatrix', 'rightMatrix'], op_name=op_name, name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []
        self.inputs = ['leftMatrix', 'rightMatrix']

class LogSoftmax(ComputationNode):
    def __init__(self, z, op_name='LogSoftmax', name=None):
        super(LogSoftmax, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class MatrixL1Reg(ComputationNode):
    def __init__(self, matrix, op_name='MatrixL1Reg', name=None):
        super(MatrixL1Reg, self).__init__(params=['matrix'], op_name=op_name, name=name)
        self.matrix = matrix
        self.params_with_defaults = []
        self.inputs = ['matrix']

class MatrixL2Reg(ComputationNode):
    def __init__(self, matrix, op_name='MatrixL2Reg', name=None):
        super(MatrixL2Reg, self).__init__(params=['matrix'], op_name=op_name, name=name)
        self.matrix = matrix
        self.params_with_defaults = []
        self.inputs = ['matrix']

class Mean(ComputationNode):
    def __init__(self, dataVectorSequence, op_name='Mean', name=None):
        super(Mean, self).__init__(params=['dataVectorSequence'], op_name=op_name, name=name)
        self.dataVectorSequence = dataVectorSequence
        self.params_with_defaults = []
        self.inputs = ['dataVectorSequence']

class Minus(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, op_name='Minus', name=None):
        super(Minus, self).__init__(params=['leftMatrix', 'rightMatrix'], op_name=op_name, name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []
        self.inputs = ['leftMatrix', 'rightMatrix']

class Negate(ComputationNode):
    def __init__(self, input, op_name='Negate', name=None):
        super(Negate, self).__init__(params=['input'], op_name=op_name, name=name)
        self.input = input
        self.params_with_defaults = []
        self.inputs = ['input']

class PackedIndex(ComputationNode):
    def __init__(self, targetObject, indexSequence, op_name='PackedIndex', name=None):
        super(PackedIndex, self).__init__(params=['targetObject', 'indexSequence'], op_name=op_name, name=name)
        self.targetObject = targetObject
        self.indexSequence = indexSequence
        self.params_with_defaults = []
        self.inputs = ['targetObject', 'indexSequence']

class Pass(ComputationNode):
    def __init__(self, x, op_name='Pass', name=None):
        super(Pass, self).__init__(params=['x'], op_name=op_name, name=name)
        self.x = x
        self.params_with_defaults = []
        self.inputs = ['x']

class PerDimMeanVarDeNormalization(ComputationNode):
    def __init__(self, dataVectorSequence, meanVector, invStdDevVector, op_name='PerDimMeanVarDeNormalization', name=None):
        super(PerDimMeanVarDeNormalization, self).__init__(params=['dataVectorSequence', 'meanVector', 'invStdDevVector'], op_name=op_name, name=name)
        self.dataVectorSequence = dataVectorSequence
        self.meanVector = meanVector
        self.invStdDevVector = invStdDevVector
        self.params_with_defaults = []
        self.inputs = ['dataVectorSequence', 'meanVector', 'invStdDevVector']

class PerDimMeanVarNormalization(ComputationNode):
    def __init__(self, dataVectorSequence, meanVector, invStdDevVector, op_name='PerDimMeanVarNormalization', name=None):
        super(PerDimMeanVarNormalization, self).__init__(params=['dataVectorSequence', 'meanVector', 'invStdDevVector'], op_name=op_name, name=name)
        self.dataVectorSequence = dataVectorSequence
        self.meanVector = meanVector
        self.invStdDevVector = invStdDevVector
        self.params_with_defaults = []
        self.inputs = ['dataVectorSequence', 'meanVector', 'invStdDevVector']

class Plus(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, op_name='Plus', name=None):
        super(Plus, self).__init__(params=['leftMatrix', 'rightMatrix'], op_name=op_name, name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []
        self.inputs = ['leftMatrix', 'rightMatrix']

class Reciprocal(ComputationNode):
    def __init__(self, z, op_name='Reciprocal', name=None):
        super(Reciprocal, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class RectifiedLinear(ComputationNode):
    def __init__(self, z, op_name='RectifiedLinear', name=None):
        super(RectifiedLinear, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class ReduceSum(ComputationNode):
    def __init__(self, z, axis=0, op_name='ReduceSum', name=None):
        super(ReduceSum, self).__init__(params=['z', 'axis'], op_name=op_name, name=name)
        self.z = z
        self.axis = axis
        self.params_with_defaults = ['axis']
        self.inputs = ['z']

class ReduceMax(ComputationNode):
    def __init__(self, z, axis=0, op_name='ReduceMax', name=None):
        super(ReduceMax, self).__init__(params=['z', 'axis'], op_name=op_name, name=name)
        self.z = z
        self.axis = axis
        self.params_with_defaults = ['axis']
        self.inputs = ['z']

class ReduceMin(ComputationNode):
    def __init__(self, z, axis=0, op_name='ReduceMin', name=None):
        super(ReduceMin, self).__init__(params=['z', 'axis'], op_name=op_name, name=name)
        self.z = z
        self.axis = axis
        self.params_with_defaults = ['axis']
        self.inputs = ['z']

class ReduceLogSum(ComputationNode):
    def __init__(self, z, axis=0, op_name='ReduceLogSum', name=None):
        super(ReduceLogSum, self).__init__(params=['z', 'axis'], op_name=op_name, name=name)
        self.z = z
        self.axis = axis
        self.params_with_defaults = ['axis']
        self.inputs = ['z']

class Scale(ComputationNode):
    def __init__(self, scalarScalingFactor, matrix, op_name='Scale', name=None):
        super(Scale, self).__init__(params=['scalarScalingFactor', 'matrix'], op_name=op_name, name=name)
        self.scalarScalingFactor = scalarScalingFactor
        self.matrix = matrix
        self.params_with_defaults = []
        self.inputs = ['scalarScalingFactor', 'matrix']

class ScatterPacked(ComputationNode):
    def __init__(self, cond, indexSequence, sourceData, op_name='ScatterPacked', name=None):
        super(ScatterPacked, self).__init__(params=['cond', 'indexSequence', 'sourceData'], op_name=op_name, name=name)
        self.cond = cond
        self.indexSequence = indexSequence
        self.sourceData = sourceData
        self.params_with_defaults = []
        self.inputs = ['cond', 'indexSequence', 'sourceData']

class Sigmoid(ComputationNode):
    def __init__(self, z, op_name='Sigmoid', name=None):
        super(Sigmoid, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class Sin(ComputationNode):
    def __init__(self, z, op_name='Sin', name=None):
        super(Sin, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class Hardmax(ComputationNode):
    def __init__(self, z, op_name='Hardmax', name=None):
        super(Hardmax, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class Sqrt(ComputationNode):
    def __init__(self, z, op_name='Sqrt', name=None):
        super(Sqrt, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class SquareError(ComputationNode):
    def __init__(self, aMatrix, anotherMatrix, op_name='SquareError', name=None):
        super(SquareError, self).__init__(params=['aMatrix', 'anotherMatrix'], op_name=op_name, name=name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix
        self.params_with_defaults = []
        self.inputs = ['aMatrix', 'anotherMatrix']

class SumColumnElements(ComputationNode):
    def __init__(self, z, op_name='SumColumnElements', name=None):
        super(SumColumnElements, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class SumElements(ComputationNode):
    def __init__(self, matrix, op_name='SumElements', name=None):
        super(SumElements, self).__init__(params=['matrix'], op_name=op_name, name=name)
        self.matrix = matrix
        self.params_with_defaults = []
        self.inputs = ['matrix']

class Tanh(ComputationNode):
    def __init__(self, z, op_name='Tanh', name=None):
        super(Tanh, self).__init__(params=['z'], op_name=op_name, name=name)
        self.z = z
        self.params_with_defaults = []
        self.inputs = ['z']

class TimeReverse(ComputationNode):
    def __init__(self, vectorSequence, op_name='TimeReverse', name=None):
        super(TimeReverse, self).__init__(params=['vectorSequence'], op_name=op_name, name=name)
        self.vectorSequence = vectorSequence
        self.params_with_defaults = []
        self.inputs = ['vectorSequence']

class TransposeTimes(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, op_name='TransposeTimes', name=None):
        super(TransposeTimes, self).__init__(params=['leftMatrix', 'rightMatrix'], op_name=op_name, name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []
        self.inputs = ['leftMatrix', 'rightMatrix']

class Where(ComputationNode):
    def __init__(self, cond, op_name='Where', name=None):
        super(Where, self).__init__(params=['cond'], op_name=op_name, name=name)
        self.cond = cond
        self.params_with_defaults = []
        self.inputs = ['cond']

Parameter = LearnableParameter
ReconcileMBLayout = ReconcileDynamicAxis
ColumnwiseCrossProduct = KhatriRaoProduct
ClassificationError = ErrorPrediction
Delay = PastValue
class ConstantTensor(ParameterTensor):
    def __init__(self, value, dims,  op_name='ConstantTensor', name=None):
        super(ConstantTensor, self).__init__(dims, learningRateMultiplier=0, init='fixedValue', value=value, op_name=op_name, name=name)
        self.params=['value', 'dims']
        self.params_with_defaults = []

class RowSlice(Slice):
    def __init__(self, beginIndex, numRows, input,  op_name='RowSlice', name=None):
        super(RowSlice, self).__init__(beginIndex, beginIndex + numRows, input, axis=1, op_name=op_name, name=name)
        self.params=['beginIndex', 'numRows', 'input']
        self.params_with_defaults = []

class ReshapeDimension(NewReshape):
    def __init__(self, x, axis, tensorShape,  op_name='ReshapeDimension', name=None):
        super(ReshapeDimension, self).__init__(x, tensorShape, beginAxis=axis, endAxis=axis + 1, op_name=op_name, name=name)
        self.params=['x', 'axis', 'tensorShape']
        self.params_with_defaults = []

class FlattenDimensions(NewReshape):
    def __init__(self, x, axis, num,  op_name='FlattenDimensions', name=None):
        super(FlattenDimensions, self).__init__(x, 0, beginAxis=axis, endAxis=axis + num, op_name=op_name, name=name)
        self.params=['x', 'axis', 'num']
        self.params_with_defaults = []

class SplitDimension(ReshapeDimension):
    def __init__(self, x, axis, N,  op_name='SplitDimension', name=None):
        super(SplitDimension, self).__init__(x, axis, '<not yet supported>', op_name=op_name, name=name)
        self.params=['x', 'axis', 'N']
        self.params_with_defaults = []

class Transpose(TransposeDimensions):
    def __init__(self, x,  op_name='Transpose', name=None):
        super(Transpose, self).__init__(x, 1, 2, op_name=op_name, name=name)
        self.params=['x']
        self.params_with_defaults = []

