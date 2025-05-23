import torch

state_dict = torch.load('TPS-ResNet-BiLSTM-Attn.pth', map_location='cpu')

if 'opt' in state_dict:
    print("Character set from model:", state_dict['opt'].character)
else:
    print("Could not find 'opt' in state_dict.")