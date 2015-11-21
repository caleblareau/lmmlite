#!/usr/bin/env python
#
# script to study pylmm results more closely:
# for each phenotype, calculate log likelihoods on a grid
# save just phenotype, method, hsq, loglik

import lmm
import numpy

# load the datasets
kinship = numpy.genfromtxt('kinship.csv', delimiter=',')
pheno =   numpy.genfromtxt('pheno.csv', delimiter=',')
covar =   numpy.genfromtxt('covar.csv', delimiter=',')

# function to print results
def print_result(result, index, method, hsq):
    result_arr = [result[0], result[1][0,0], result[1][1,0], result[2][0,0], result[3]]
    for j in range(len(result_arr)):
        result_arr[j] = str(result_arr[j])
    print(','.join([str(index), method] + result_arr))

# values 0, 0.01, 0.02, ..., 1.0
n_val = 101
hsq_vec = [x/(n_val-1) for x in range(n_val)]

print('index,method,hsq,loglik') # header
for i in range(pheno.shape[1]):
    obj = lmm.LMM(pheno[:,[i]], kinship, X0=covar)
    ll = [obj.LL(hsq, REML=True)[0] for hsq in hsq_vec]
    for j in range(n_val):
        print(",".join([str(i+1), "reml", str(hsq_vec[j]), str(ll[j])]))

    ll = [obj.LL(hsq, REML=False)[0] for hsq in hsq_vec]
    for j in range(n_val):
        print(",".join([str(i+1), "ml", str(hsq_vec[j]), str(ll[j])]))