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
  # temp = matrix
  # result = []
  for parent, i in enumerate(matrix):
    for child, index in enumerate(matrix):
      matrix[i][index] = matrix[index][i]
