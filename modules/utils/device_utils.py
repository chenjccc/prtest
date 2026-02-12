def get device(svc index: int = 0):
"device"
if torch.npu.is available():
device = torch.device(f"npu:{int(svc index)}")
torch.npu.set device(device)
print(f"using npu: {device}")
elif torch.cuda.is available():
device = torch.device(f"cuda:{int(svc index)}")
print(f"using cuda:fdevice}")
elif torch.backends.mps.is available():
device = torch.device("mps")
print(f"using mps")
else:
device = torch.device("cpu")
print("using cpu")
return device
