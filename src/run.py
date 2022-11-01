import torch
from codebert.unixcoder import UniXcoder



def data_loader(path):







func = "def f(a,b): if a>b: return a else return b"
tokens_ids = model.tokenize([func],max_length=512,mode="<encoder-only>")
source_ids = torch.tensor(tokens_ids).to(device)
tokens_embeddings,max_func_embedding = model(source_ids)


def get_encoder():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = UniXcoder("microsoft/unixcoder-base")
    model.to(device)



def train():



if __name__=="__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

