#!/usr/bin/ env python
# coding=utf-8

import sys

def auc(labels,predicted_ctr):
  print predicted_ctr
  i_sorted = sorted(range(len(predicted_ctr)),key=lambda i:predicted_ctr[i],reverse=True)
  #i_sorted = sorted(predicted_ctr)
  #print i_sorted
  auc_temp = 0.0
  tp = 0.0
  tp_pre = 0.0
  fp = 0.0
  fp_pre = 0.0
  last_value = predicted_ctr[i_sorted[0]]
  for i in range(len(labels)):
    if labels[i_sorted[i]] > 0:
      tp += 1
    else:
      fp += 1
    if last_value != predicted_ctr[i_sorted[i]]:
      auc_temp += (tp + tp_pre) * (fp - fp_pre) / 2.0
      tp_pre = tp
      fp_pre = fp
      last_value = predicted_ctr[i_sorted[i]]
  auc_temp += (tp + tp_pre) * (fp - fp_pre) / 2.0
  return auc_temp / ( tp * fp)

def evaluate(ids,true_values,predict_values):
  labels = []
  predicted_ctr = []
  for i in range(len(ids)):
    labels.append(int(true_values[i]))
    predicted_ctr.append(float(predict_values[i]))
  return auc(labels,predicted_ctr)


if __name__ == "__main__":
  f = open("test_pctr","r") #sys.argv[1]
  ids = []
  true_values = []
  predict_values = []
  for line in f:
    seg = line.strip().split(",")
    ids.append(seg[0])
    true_values.append(seg[1])
    predict_values.append(seg[2])
  print evaluate(ids,true_values,predict_values)