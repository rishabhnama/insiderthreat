# Script to evaluate GNN model

def evaluate_model(model, data):
    model.eval()
    out = model(data.x, data.edge_index)
    pred = out.argmax(dim=1)
    correct = pred[data.test_mask] == data.y[data.test_mask]
    accuracy = int(correct.sum()) / int(data.test_mask.sum())
    print(f"Test Accuracy: {accuracy:.4f}")
