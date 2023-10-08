# Create a directory for YOLOv6 if it doesn't exist and clone the YOLOv6 repository
! mkdir -p /content/drive/MyDrive/yolov6
! git clone https://github.com/meituan/YOLOv6 /content/drive/MyDrive/yolov6

# Change directory to the YOLOv6 folder
cd /content/drive/MyDrive/yolov6

# Install the required Python packages
! pip install -r requirements.txt

# Download YOLOv6 weights
! wget https://github.com/meituan/YOLOv6/releases/download/0.4.0/yolov6s.pt

# Train YOLOv6 model
! python tools/train.py --batch 16 --conf configs/yolov6s_finetune.py --data /content/drive/MyDrive/dataset/dataset.yaml --device 0 --epochs 100

# Evaluate YOLOv6 model
! python tools/eval.py --data /content/drive/MyDrive/dataset/dataset.yaml --weights /content/drive/MyDrive/yolov6/runs/train/exp/weights/best_ckpt.pt --device 0

# Import necessary libraries for the next sections
import os
import subprocess

# Paths to YOLOv6 weights, YAML file, and the list of source directories/files
weights_path = '/content/drive/MyDrive/yolov6/runs/train/exp/weights/best_ckpt.pt'
yaml_path = '/content/drive/MyDrive/dataset/dataset.yaml'

# Define source paths for the first dataset
source_paths_1 = [
    '/content/drive/MyDrive/Auto-WCEBleedGen Challenge Test Dataset/Test Dataset 1',
    # Add more source paths as needed
]

# Device (0 for GPU, 'cpu' for CPU)
device = 0

# Loop through each source and run YOLOv6 inference for the first dataset
for source_path in source_paths_1:
    command = [
        'python', 'tools/infer.py',
        '--weights', weights_path,
        '--source', source_path,
        '--yaml', yaml_path,
        '--device', str(device)
    ]

    subprocess.run(command)

# Define source paths for the second dataset (if needed)
source_paths_2 = [
    '/content/drive/MyDrive/dataset/images/val',
    # Add more source paths as needed
]

# Loop through each source and run YOLOv6 inference for the second dataset (if needed)
for source_path in source_paths_2:
    command = [
        'python', 'tools/infer.py',
        '--weights', weights_path,
        '--source', source_path,
        '--yaml', yaml_path,
        '--device', str(device)
    ]

    subprocess.run(command)

# Define source paths for the third dataset (if needed)
source_paths_3 = [
    '/content/drive/MyDrive/Auto-WCEBleedGen Challenge Test Dataset/Test Dataset 2',
    # Add more source paths as needed
]

# Loop through each source and run YOLOv6 inference for the third dataset (if needed)
for source_path in source_paths_3:
    command = [
        'python', 'tools/infer.py',
        '--weights', weights_path,
        '--source', source_path,
        '--yaml', yaml_path,
        '--device', str(device)
    ]

    subprocess.run(command)
