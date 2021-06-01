from csv import reader # For reading csv
from matplotlib import pyplot as plt    # For plotting graph

class Drawdown:

	def __init__(self):
		self.openingTime = 0
		self.closingTime = 0
		self.recoveryTime = 0
		self.peak = 0

	def set_opening_time(self, time):
		self.openingTime = time

	def set_closing_time(self, time, peak):
		self.closingTime = time
		self.peak = peak
		self.recoveryTime = self.closingTime - self.openingTime


class CSVfile:
	def __init__(self, fileName):
		self.data = None

		with open (fileName) as csvfile:
			rows = reader(csvfile)
			res = list(zip(rows))

			# CSV File contains Date,Close/Last,Volume,Open,High,Low
			# Extracting column 1(Close/Last) for pnl values from row 1 after header

			self.data = [ float(i[0][1].strip('$')) for i in reversed(res[1:]) ]	
			self.header = res[0][0][1]

if __name__ == '__main__':

	# File to read data from
	csvFile = CSVfile("HistoricalData_6m.csv")				
	# csvFile = CSVfile("HistoricalData_5y.csv")				


	movingMax = csvFile.data[0] # used for computing drawdownValue at every point

	drawdownValues = [] # Used for graph plotting, drawdown at all points (from formula)
	currentDrawdownPeak = 0

	drawdownObjects = []

	for time, pnl in enumerate(csvFile.data):

		movingMax = max(pnl, movingMax)

		drawdownValues.append(((movingMax - pnl)/movingMax)*100)

		currentDrawdownPeak = max(drawdownValues[time], currentDrawdownPeak)

		# Drawdown starts rising from zero
		if drawdownValues[time-1] == 0 and drawdownValues[time]!=0:

			drawdownObject = Drawdown()
			drawdownObject.set_opening_time(time - 1)
			currentDrawdownPeak = drawdownValues[time]

		# Drawdown ends, closes to zero
		if drawdownValues[time-1]!=0 and drawdownValues[time] == 0:

			drawdownObject.set_closing_time(time, currentDrawdownPeak)
			
			currentDrawdownPeak = 0
			drawdownObjects.append(drawdownObject)
			drawdownObject = None


	for drawdownObject in drawdownObjects:
		print("Drawdown from t = {} to t = {}, depth = {}%, recovery time = {} ".\
			format(drawdownObject.openingTime, drawdownObject.closingTime,\
			 round(drawdownObject.peak, 3), drawdownObject.recoveryTime))

	print("Total drawdowns = {}".format(len(drawdownObjects)))

	# Plotting graph
	plt.plot(drawdownValues)
	plt.show()
		


