# [Auto-WCEBleedGen-Challenge](https://misahub.in/CVIP/challenge.html)
<b>1. Classification Folder contains:</b>
  -  Model folder
     -  "Train and Test.py" contains the code for Train , validation and Testing for the datasets provided.
     -  "CNN2d.h5"  is saved model file size of 1.53Mb which is a Lightweight Architecture.
     -  "extracted_features_Using_DenseNet 121" contains the features we extracted from the original images using Densenet121 to train the model well.
  -  Output folder
     - contains different Metric evaluations (ROC Curve , Confusion Matrix , Model loss and Accuracy plots , Accuracy, F1 score , Recall )
  -  Pictures folder
     - 5 best images selected from testing dataset 1 and 2 separately , 10 best images and interpretability plot(CAM)  from Validation  showing its classification
  - Data Profiling report
     - the process of examining, analyzing, reviewing and summarizing data sets to gain insight into the quality of data
     - Click the link above to view the Data Profiling Report in your browser [Data Profiling Report](https://htmlpreview.github.io/?https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/blob/main/Classification/Data%20Profiling%20report/Data_Profiling_report.html)
 - For More Clear Understanding
    - Click here to check the notebook [Jupyter Notebook link](https://colab.research.google.com/drive/1NcEQ4AYXAuyDBVPScWmfjxFpnu9zSOsT?usp=sharing)   

Note: Due to the fact that we employed programmatic code to save the data profiling report in HTML, please take note. Consequently, there are almost 10,000 lines of HTML code, making up 98% of the entire language. Just ignore it.
       
## Classification Metrics

Metrics                 | Value
---------------------- | -------------
Accuracy               | 98.85
Recall                 | 99.62
F1 Score               | 98.87



# Validation Dataset Showing Its Classification

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/1ecf1cfa-dfa8-4c20-a34c-9170b864a0a9" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/eaed66b1-192b-41b5-a996-3a0816e22ddf" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/9d1a80de-df51-4973-9627-3b8d386e93b8" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/adc1ef73-efa3-4c98-adc2-2352eb84d6a0" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/ebc3c33a-1b57-4ff6-8c35-8f454553c7c6" width="300px">
      <br>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/d5d6cecb-8c4e-48b1-8128-7c3a962c661b" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/da523e36-f364-4ed5-b55a-c9688e56f8dc" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/716987ea-36d1-4eab-84b8-d6a2d6acd4cf" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/2450bb55-6a2d-439c-ba70-0e4bad499162" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/0cc3ca9f-6773-40fd-ba74-4c82611bd299" width="300px">
      <br>
    </td>
  </tr>
</table>

# Testing Dataset Showing Its Classification
# Test Dataset 1
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/3f924699-e2a2-424e-b9fe-3d347fec4fc2"width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/ef667f2e-64d3-4471-b2e9-c129acaa4c60" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/cbb9145c-8e46-492e-a8a0-695756bc2f7f" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/a83cc461-b320-4b00-9c52-925e74521724" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/ed450009-3998-459f-b124-1046443b1910" width="300px">
      <br>
    </td>
  </tr>
</table>

# Test Dataset 2
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/eaf9ac46-8eb1-468e-9609-03fdd3e237c4" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/3d5e61d7-92f0-41fb-85e3-9985c0f3e052" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/8a09bd32-5aa9-4622-8c7b-da5be3c88d39" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/6476bc47-776b-438d-b8d0-4bcee9d2dc00" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/117301325/e5b5c2f9-22ff-43ce-9514-5246d343d125" width="300px">
      <br>
    </td>
  </tr>
</table>


<b>2. Detection Folder contains:</b>
  -  Weights folder
     -  contains the "best_ckpt.pt" yolov6 model saved.
  -  Output folder
     - contains different Metric evaluations ( AP, MAP, IOU )
  -  Pictures folder
     - 5 best images selected from testing dataset 1 and 2 separately , 10 best images from Validation  showing its detection with confidence level
  - CAM Plot folder
     - contains 10 best images of interpretability plot(CAM) for Validation, test datasets
   -  dataset.yaml
      - defining the configuration and structure of the custom dataset
  -  prediction_validation.csv
     -  showing bbox's with confidence level on validation dataset
  - yolov6_detection.py
     - contains the code for Train , Test and Validation on Dataset to perform Detection

    
## Detection Metrics

Metrics                           | Value
--------------------------------- | -------------
Average Precision                 | 65.50
Mean Average Precision            | 61.51
Intersection over Union           | 0.50


# Validation Dataset Showing Its Detection

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/0262e598-946c-4eb7-b14c-a38bd170c074" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/d199075d-b909-4bb2-a9d4-954349d4ef9c" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/4d8a047a-d8c2-4ade-a170-01b84d6013b6" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/f2290b25-18c7-4a53-b6eb-7a07d9e7ec21" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/aec8627f-8859-41e5-bbac-60729c5f7899" width="300px">
      <br>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/510081c5-dd43-464e-a168-ecb2d62a4f80" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/d87b6826-1b07-4d0b-a702-3a80c8ccb05b" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/05677fe5-55c6-45d0-ab1b-12957fe27223" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/fe784393-e14b-4223-ad97-edbcfad8c6cd" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/54e1a9c7-f567-4cbb-8e21-147909445743" width="300px">
      <br>
    </td>
  </tr>
</table>

# Testing Dataset Showing Its Detection
# Test Dataset 1
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/e45bd057-a7b9-4307-bd04-03056362a0d5"width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/ad38f74d-e1b8-433d-8f4f-38a02a3db84f" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/cc2197ec-5ffa-42e9-bab0-b4fe658424eb" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/efdf97d2-8d3f-4d38-842e-f0866c42e9d8" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/5c44dead-c0d1-4900-a162-b2068217f0d1" width="300px">
      <br>
    </td>
  </tr>
</table>

# Test Dataset 2
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/d3f07121-670c-440d-8a4a-54b2543efe92" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/3f24f101-030a-4588-96c7-499aa4acd2a9" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/90b01382-e675-4d55-9d7d-8b484b3883d9" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/84f706b7-73bd-466d-acf0-401b71128814" width="300px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/418c5858-8b07-4b35-8ca9-a84e4dd26ece" width="300px">
      <br>
    </td>
  </tr>
</table>



# Validation Dataset Showing Its Interpretability Plot (CAM)
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/90050adc-5cef-4992-9ba1-746e67cf44af" width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/af331ba9-0866-406d-9d28-489d7a9a06cc" width="650px">
      <br>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/9a57cb32-a6af-4fcb-a71b-41a22e30f901"width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/9de7e2b2-00e8-4d8c-9bf5-2f3cd7fd2643" width="650px">
      <br>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/40df3e9d-0d93-4450-b0a9-6322aeed40f6"width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/c97dc649-a6df-498a-9766-5bceb759d709" width="650px">
      <br>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/be428225-d562-451f-8801-7fc927d97472" width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/58a8eae0-8e00-430e-ae03-35d6ab7ca78c" width="650px">
      <br>
    </td>
    </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/0aff6836-8ba2-406e-9bc3-adeec29d23c3" width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/6e7d3ca5-00e3-457a-a744-c29040465490" width="650px">
      <br>
    </td>
    </tr>
</table>






# Testing Dataset Showing Its Interpretability Plot (CAM)
# Test Dataset 1
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/e7c5aab8-712f-4202-a233-2fe8f502c785"width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/ce2f628e-6770-41e9-86bd-86a0226cb303" width="650px">
      <br>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/b5cf7d1a-b12a-4a32-841f-a7289a8c2a0c"width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/34feb37d-1f11-4f34-827e-49d2c21a70d5" width="650px">
      <br>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/d88c62f8-e89f-48ab-a023-803ea6d90997"width="480px">
      <br>
    </td>
  </tr>
</table>

# Test Dataset 2
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/a0e06349-dc51-4cc8-9802-85af87db7a86" width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/c988d814-2db6-43cc-b4bb-bcf06641520d" width="650px">
      <br>
    </td>
    </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/eb2c4404-c3d3-4829-9c55-199f205bab83" width="650px">
      <br>
    </td>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/f0818d32-61ff-41e6-92b8-a5629ae5a7b1" width="650px">
      <br>
    </td>
    </tr>
</table>
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/assets/143547473/40cb467e-000b-4a39-9987-855be0b88b02" width="480px">
      <br>
    </td>
  </tr>
</table>

<b>3. Excel Sheet Submission:</b>
- The Excel sheet containing the image IDs and predicted class labels of testing dataset 1 is saved as <b>"test_dataset_1_predictions.xlsx"</b> 
 [click me to download <b>"test_dataset_1_predictions.xlsx"</b>](https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/blob/main/test_dataset_1_predictions.xlsx)

- The Excel sheet containing the image IDs and predicted class labels of testing dataset 2 is saved as <b>"test_dataset_2_predictions.xlsx"</b> 
 [click me to download <b>"test_dataset_2_predictions.xlsx"</b>](https://github.com/kasamrohith02/Auto-WCEBleedGen-Challenge/blob/main/test_dataset_2_predictions.xlsx)

