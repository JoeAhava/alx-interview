#!/usr/bin/env python3
'''
Rotate and n x n matrix
'''


def rotate_2d_matrix(matrix):
  '''
  given nxn matrix
  this rotates it
  '''
  n = len(matrix)
  result = []
  for parent in enumerate(matrix):
    temp = []
    for child in enumerate(matrix):
      
