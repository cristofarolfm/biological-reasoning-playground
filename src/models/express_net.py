import torch, torch.nn as nn

class ExpressNet(nn.Module):
    def __init__(self, in_dim, hidden=16, out_dim=2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.ReLU(),
            nn.Linear(hidden, out_dim)
        )
    def forward(self, x): 
        return self.net(x)
