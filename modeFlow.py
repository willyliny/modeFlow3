from taskflow import engines
from taskflow.patterns import linear_flow
import TaskPool
from FlowPool import UnorderedAlertFlow

class Mode3Flow():
    def __init__(self, shadowModel):
        self.shadowModel = shadowModel
        self.mode3Flow = linear_flow.Flow(self.__class__.__name__)
        self.unorderedAlertFlow = UnorderedAlertFlow(self.__class__.__name__, "Yolo").buildFlow()
    
    def buildFlow(self):
        self.mode3Flow.add(
            TaskPool.frameTask(self.__class__.__name__ + '_frameTask', provides = "frame"),
            TaskPool.yoloTask(self.__class__.__name__ + '_yoloTask', requires = "frame", provides = "Yolo"),
            self.unorderedAlertFlow 
        )
        result = engines.load(self.mode3Flow, store={'shadowModel':self.shadowModel}, engine = "parallel")
        result.run()

def runFlow(shadowModel):
	Mode3Flow(shadowModel).buildFlow()
