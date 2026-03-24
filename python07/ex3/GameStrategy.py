from abc import ABC, abstractmethod
from ex0.Card import Card
from ex1.SpellCard import SpellCard

class GameStrategy(ABC):
	def __init__(self, strategy: str):
		self.strategy = strategy

	@abstractmethod
	def execute_turn(self, hand: list, battlefield: list) -> dict:
		pass

	@abstractmethod
	def get_strategy_name(self) -> str:
		pass


	@abstractmethod
	def prioritize_targets(self, available_targets: list) -> list:
		pass
