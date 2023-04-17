import pandas as pd 
from abc import ABC, abstractmethod

class Model(ABC):
      def __init__(
          self, 
          random_state: int,
      ):
          self.random_state = random_state

      @abstractmethod
      def train(self):
          pass

      @abstractmethod
      def test(self):
          pass

      @abstractmethod
      def results(self, predictions: list, true_values: list, print_title: str, plot_title: str) -> dict:
          pass