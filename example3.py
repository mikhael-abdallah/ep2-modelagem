import numpy as np

from kivy.app import App
from kivy.uix.widget import Widget
from kivy_garden.graph import Graph, LinePlot
from kivy.clock import Clock


class Example3(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.numbers = []
        self.time_list = []
        self.time_counter = 0
        self.time_step = 0.01
        self.max_plot = 5
        self.min_plot = 0
        self.y_max_plot = 2
        self.y_min_plot = -2
        self.graph = None
        self.plot = None
        self.start_function = None

        self.start_plot()

    def start_plot(self):
        self.graph = Graph(xmin=self.min_plot, xmax=self.max_plot, ymin=self.y_min_plot, ymax=self.y_max_plot,
                           border_color=[1, 1, 1, 1], x_grid=True, y_grid=True, draw_border=True,
                           x_grid_label=True, y_grid_label=True)

        self.graph.background_color = 0, 0, 0, 1
        self.ids.box.add_widget(self.graph)
        self.plot = LinePlot(color=[1, 1, 1, 1])
        self.graph.add_plot(self.plot)

    def start(self):
        self.ids.start_button.state = "down"
        self.ids.start_button.disabled = True
        self.start_function = Clock.schedule_interval(self.update_label, self.time_step)

    def stop(self):
        if self.start_function:
            self.start_function.cancel()
            self.ids.start_button.state = "normal"
            self.ids.start_button.disabled = False

    def update_label(self, *args):
        self.numbers.append(self.generate_number())
        self.time_list.append(self.time_counter)
        self.time_counter += self.time_step

        if len(self.numbers) * self.time_step > self.max_plot:
            self.reset_plot()

        self.plot.points = [(self.time_list[i], self.numbers[i]) for i in range(len(self.numbers))]

    def clear_plot(self):
        self.ids.box.clear_widgets()
        self.start_plot()
        self.reset__plot()

    def reset_plot(self):
        self.numbers = []
        self.time_counter = 0
        self.time_list = []

    def generate_number(self):
        return np.random.uniform(self.y_min_plot, self.y_max_plot)


class Example3App(App):
    def build(self):
        return Example3()


if __name__ == "__main__":
    Example3App().run()
