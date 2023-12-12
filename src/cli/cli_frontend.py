from rich.live import Live
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.highlighter import RegexHighlighter
from time import sleep
from rich.theme import Theme
from rich.align import Align
from rich.table import Table


class NumberHighlighter(RegexHighlighter):
	base_style = "number."
	highlights = [r"(?P<square>#)"]


class cli:
	def __init__(self):
		self.console = Console()
	
	def log(self, x):
		self.console.print(x)
		
	def error(self, x):
		raise Exception(x)

	def info(self, x, wait):
		self.console.print(Markdown(x))
		if wait:
			input("\npress enter to continue")

	def count_down(self, rc):
		theme = Theme({"number.square": "green on green"})
		highlighter = NumberHighlighter()
		with Live(
			highlighter(
				Text("\n" + open(rc / "3").read())
			),
			console=Console(theme=theme),
			transient=True,
			screen=True
		) as live:
			sleep(1)
			live.update(
				highlighter(
					Text("\n" + open(rc / "2").read())
				)
			)
			sleep(1)
			live.update(
				highlighter(
					Text("\n" + open(rc / "1").read())
				)
			)
			sleep(1)
			live.update(
				highlighter(
					Text("\n" + open(rc / "go").read())
				)
			)
			sleep(1)

	def print_levels(self, data):
		output = Table()
		output.add_column("Level", justify="center")
		output.add_column("Description")
		output.add_column("difficulty")
		for i in data.keys():
			level = data[i]
			dificulty = level["difficulty"]
			if dificulty == 0:
				dificulty = ("Easy", "green")
			elif dificulty == 1:
				dificulty = ("Medium", "yellow")
			elif dificulty == 2:
				dificulty = ("Hard", "red")
			elif dificulty == 3:
				dificulty = ("Extreme", "bold black on red")
			output.add_row(
				Text.assemble((i, "bold")),
				Markdown(level["description"]),
				Text.assemble(dificulty),
			)
		self.console.print(output)
