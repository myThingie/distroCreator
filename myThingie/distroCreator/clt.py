import random

class CentralLimitTheorem(object):


	def __init__(self, distribution):
		self.distribution = distribution
		self.dist_min = min(distribution)
		self.dist_max = max(distribution)

	def _sample(self, N):
		sampleSum = 0
		for i in range(N):
			sampleSum += random.choice(self.distribution)
		return float(sampleSum) / float(N)


	def run_sample_demo(self, N, plot = False, num_bins = None):
		means = []
		for i in range(1000):
			means.append(self._sample(N))

		if plot:
			title = "sample mean distribution with N = {}".format(N)
			plot_distributions(means, title, dist_min, dist_max, num_bins)
		return means

	def plot_distributions(distribution, title = None,
										bin_min = None,
										Bin_max = None, num_bins = None):
		import matplotlib.pyplot as plt
		import seaborn as sns
		sns.set_palette("deep", desat = .65)

		if num_bins != None:
			bin_size = (bin_max - bin_min) / num_bins
			manual_bins = range(bin_min, bin_max + bin_size, bin_size)
			[n, bins, patches] = plt.hist(distribution, bins = manual_bins)

		else:
			[n, bins, patches] = plt.hist(distribution)

		if title != None:
			plt.title(title)

		plt.xlim(bin_min, bin_max)
		plt.ylim(0, max(n) + 2)
		plt.ylabel("Frequency")
		plt.xlabel("Observation")
		plt.show()
