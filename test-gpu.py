import torch

print("GPU is_available:" , torch.cuda.is_available())

print("cuda.device_count:", torch.cuda.device_count())

print("cuda.current_device:",torch.cuda.current_device())

print("cuda.device:" ,torch.cuda.device(0))

print("device_name:" , torch.cuda.get_device_name(0))