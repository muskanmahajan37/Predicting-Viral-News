"""
Main file for News Popularity Prediction Task.

Assignment: Final Project
Class: Data Mining | CSC 440
Programmer: Gregory D. Hunkins 
"""
import os
import argparse
from data_utils import read_clean_data, BinaryY
from models import NeuralNet

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def main(grid):
	# Get Clean Data
	X, Y = read_clean_data()
	Y_binary = BinaryY(Y)
	NeuralNet(X, Y_binary, grid)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--grid", help="Enable grid search.", action="store_true")
	args = parser.parse_args()
	main(args.grid)
