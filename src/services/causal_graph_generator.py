from src.utils.get_data import DataSetName, get_data_from_CSV
from src.algorithm.hill_climbing import HillClimbSearch

class CausalGraphGenerator:
    def __init__(self, file_name):
        self.dataset_name = DataSetName(name = file_name)
        self.data_frame = get_data_from_CSV(self.dataset_name)
        self.causal_graph = None


    def generate_causal_graph(self, constraints=None, file_name=""):
        """
        使用因果推断库生成因果图
        :param constraints: 可选，对生成的因果图施加的约束条件
        """
        # 首先检查数据是否已经被读取
        if self.data_frame is None:
            self.data_frame = get_data_from_CSV(DataSetName(name = file_name))
        hillclimb_search = HillClimbSearch(self.data_frame)

        # 构建因果图
        self.causal_graph = hillclimb_search.estimate()


        # 这里使用所选的库生成因果图
        # 例如，使用 DoWhy 创建一个 CausalModel
        # self.causal_graph = CausalModel(
        #     data=self.data_frame,
        #     ...  # 其他参数
        # )

        # 如果有额外的约束条件，应用它们
        if constraints:
            # 应用约束条件的逻辑
            pass

        return self.causal_graph
