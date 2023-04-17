import pandas as pd 
from abc import ABC, abstractmethod

import pandas as pd 
from abc import ABC, abstractmethod
from models.model import Model

class SupervisedModel(Model, ABC):
      def __init__(
          self, 
          dataset_name: str,
          train_data_df_x: pd.DataFrame, 
          train_data_df_y: pd.DataFrame, 
          test_data_df_x: pd.DataFrame, 
          test_data_df_y: pd.DataFrame,
          random_state: int,
      ):
          super().__init__(random_state = random_state)
          self.train_data_df_x = train_data_df_x
          self.train_data_df_y = train_data_df_y 
          self.test_data_df_x = test_data_df_x
          self.test_data_df_y = test_data_df_y
          self.random_state = random_state
          self.dataset_name = dataset_name

      def train(self):
          self.model.fit(self.train_data_df_x, self.train_data_df_y)
          train_pred = self.model.predict(self.train_data_df_x)
          return self.results(train_pred, self.train_data_df_y, f'Training on {self.train_data_df_x.shape[0]} samples', f'{self.dataset_name} training results')

      def test(self):
          test_pred = self.model.predict(self.test_data_df_x)
          return self.results(test_pred, self.test_data_df_y, f'Testing on {self.test_data_df_x.shape[0]} samples', f'{self.dataset_name} testing results')

      @abstractmethod
      def results(self, predictions: list, true_values: list, print_title: str, plot_title: str) -> dict:
          pass