from sim2real.plot.plotter import Plotter

log_file = "test.json" # TODO

plotter = Plotter()
plotter.load_data(log_file)
plotter.plot()
