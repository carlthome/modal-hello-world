import modal

stub = modal.Stub("example-get-started")


pytorch = modal.Image.from_dockerhub("pytorch/pytorch")


@stub.function(image=pytorch)
def square(x):
    import torch

    print(torch.__version__)

    y = (torch.tensor(x) ** 2).item()
    return y


@stub.local_entrypoint()
def main():
    print("the square is", square.call(42))
