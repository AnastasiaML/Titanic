import pprint
import pandas as pd 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from models.supervised.supervised_model import SupervisedModel

class RandomForestClassifierModel(SupervisedModel):
      def __init__(
          self, 
          dataset_name: str,
          train_data_df_x: pd.DataFrame,
          train_data_df_y: pd.DataFrame, 
          test_data_df_x: pd.DataFrame, 
          test_data_df_y: pd.DataFrame,
          random_state: int,
      ):
          super().__init__(dataset_name = dataset_name,
                           train_data_df_x = train_data_df_x, 
                           train_data_df_y = train_data_df_y, 
                           test_data_df_x = test_data_df_x, 
                           test_data_df_y = test_data_df_y, 
                           random_state = random_state
          )
          self.model = RandomForestClassifier(random_state = random_state)
          self.model_name = 'Random Forest Classifier'

      def results(self, predictions: list, true_values: list, print_title: str, plot_title: str) -> dict:
          metrics = {
	      'accuracy_score': f'{round(accuracy_score(true_values, predictions) * 100, 2)} %',
	      'precision_score': f'{round(precision_score(true_values, predictions) * 100, 2)} %',
	      'recall_score': f'{round(recall_score(true_values, predictions) * 100, 2)} %',
              'f1_score': f'{round(f1_score(true_values, predictions) * 100, 2)} %'
          }

          print(f'\n----------- {print_title} with {self.model_name} model -----------\n')
          pprint.pprint(metrics)

          return metrics