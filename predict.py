# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:42:36 2019

@author: SY
"""
import warnings

import torch.nn

warnings.filterwarnings('ignore')
import pandas as pd
from chemprop.parsing import parse_train_args, modify_train_args
from chemprop.train import make_predictions



if __name__ == '__main__':
    args = parse_train_args()
    args.checkpoint_path = './dumped/0316-finetune/clintox/run_2/model_0/model.pt' # !
    args.num_tasks = 14   # !
    args.dataset_type = 'classification' #!
    modify_train_args(args)

    data = pd.read_csv('./Monomer.csv')  # !
    pred, smiles = make_predictions(args, data.smiles.tolist())
       
    df = pd.DataFrame({'smiles':smiles})
    for i in range(len(pred[0])):
        df[f'pred_{i}'] = [item[i] for item in pred]
    df.to_csv(f'./predict.csv', index=False)
