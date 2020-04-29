import torch
from kogpt2.pytorch_kogpt2 import get_pytorch_kogpt2_model
from gluonnlp.data import SentencepieceTokenizer
from kogpt2.utils import get_tokenizer

tok_path = get_tokenizer()
model, vocab = get_pytorch_kogpt2_model()
tok = SentencepieceTokenizer(tok_path)

def make_str(receive_str):
  toked = tok(receive_str)
  while 1 :
    print(receive_str, clone_receive_str)
    input_ids = torch.tensor([vocab[vocab.bos_token],]  + vocab[toked]).unsqueeze(0)
    pred = model(input_ids)[0]
    gen = vocab.to_tokens(torch.argmax(pred, axis=-1).squeeze().tolist())[-1]
    if gen == '</s>':
        break
    receive_str += gen.replace('▁', ' ')
    toked = tok(receive_str)
  return receive_str
    
if __name__ == "__main__":
  str1 = make_str('2019년 한해를 보내며,')
  str2 = make_str('저녁먹고')
  str3 = make_str('오늘은 날씨')

  print(str1)
  print(str2)
  print(str3)