import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import gradio as gr

data = pd.read_csv("data_daily.csv")

data["Date"] = pd.to_datetime(data["# Date"])

# Group data by month and aggregate receipt counts
monthly_data = data.groupby(data["Date"].dt.month)["Receipt_Count"].sum().reset_index()


class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


model = LinearRegressionModel()

X = torch.FloatTensor(monthly_data["Date"].values).view(-1, 1)
y = torch.FloatTensor(monthly_data["Receipt_Count"].values).view(-1, 1)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


# Function for gradio interface
def predict_receipts(month):
    month_tensor = torch.FloatTensor([month])
    if month > 12 or month < 1:
        return "Error: Month must be between 1 and 12"
    with torch.no_grad():
        prediction = model(month_tensor).item()

    return prediction


iface = gr.Interface(fn=predict_receipts, inputs="number", outputs="textbox")
iface.launch(server_name="0.0.0.0")
