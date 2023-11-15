from sim2real.plot.plot import Plotter

log_file = "2023-11-15-14-08-53.json" # TODO

plotter = Plotter()
plotter.load_data(log_file)
plotter.plot()
