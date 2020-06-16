import pandas as pd
from mlpm_present.data.data_utils import *

trainSim = pd.read_csv("./data/MZVAV-2-2.csv",index_col=0,parse_dates=True)
dataReal = pd.read_csv("./data/MZVAV-2-1.csv",index_col=0,parse_dates=True)

trainSim.columns = column_names
dataReal.columns = column_names

# Always at 1.4 0 change, can be omitted
trainSim.drop("staticPresSp", inplace=True,axis=1)
dataReal.drop("staticPresSp", inplace=True,axis=1)

# For the simulated data 100% correlated with ocMode
trainSim.drop("returnFanStat", inplace=True, axis=1)
dataReal.drop("returnFanStat", inplace=True, axis=1)

trainSim["month"] = trainSim.index.month
trainSim["hour"] = trainSim.index.hour

dataReal["month"] = dataReal.index.month
dataReal["hour"] = dataReal.index.hour

trainSim.loc[healthy, "label"] = 0
trainSim.loc[wrong_1, "label"] = 1
trainSim.loc[wrong_2, "label"] = 2
trainSim.loc[wrong_3, "label"] = 3

y_label = trainSim.loc[:, "label"]

# Slicing the Simulated data
healthyTrain = trainSim.loc[healthy, :]
unhealthyTrain = trainSim.loc[unhealthy, :]

healthyTrainSimOc = healthyTrain.loc[healthyTrain["ocModeInd"] == 1]
healthyTrainSimUnOc = healthyTrain.loc[healthyTrain["ocModeInd"] == 0]

unhealthyTrainSimOc = unhealthyTrain.loc[unhealthyTrain["ocModeInd"] == 1]
unhealthyTrainSimUnOc = unhealthyTrain.loc[unhealthyTrain["ocModeInd"] == 0]

trainOC = trainSim.loc[trainSim["ocModeInd"] == 1, :]
trainUnOc = trainSim.loc[trainSim["ocModeInd"] == 0, :]

dataReal.loc[dataReal.loc[:,"faultGT"]==0,"label"] = 0
dataReal.loc[wrong_exp,"label"] = 2

# Slicing the Real data
healthyExp = dataReal.loc[healthy_exp,:]
unhealthyExp = dataReal.loc[wrong_exp,:]

healthyExpOc = healthyExp.loc[healthyExp["ocModeInd"] == 1]
healthyExpUnOc = healthyExp.loc[healthyExp["ocModeInd"] == 0]

unhealthyExpOc = unhealthyExp.loc[unhealthyExp["ocModeInd"] == 1]
unhealthyExpUnOc = unhealthyExp.loc[unhealthyExp["ocModeInd"] == 0]


y_exp = dataReal.loc[:,"label"]

expOC = dataReal.loc[dataReal["ocModeInd"] == 1, :]
expUnOc = dataReal.loc[dataReal["ocModeInd"] == 0, :]