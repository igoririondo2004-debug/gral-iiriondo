import kagglehub

# Download latest version
path = kagglehub.dataset_download("titericz/imagenet1k-val")

print("Path to dataset files:", path)
