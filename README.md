# Fine tuning EasyOCR Model

## 1.Download the TextRecognitionDataGenerator

## 2.Install the dependencies in a virtual enviornment.

## 3.Use the following command to generate arabic dataset
trdg -l ar -c 1000 -w 1

## 4.To train the model the the data created using TRDG must be converted into lmdb dataset
   python create_lmdb_dataset.py \
   /Users/ajit/deep-text-recognition-benchmark/out \
   /Users/ajit/deep-text-recognition-benchmark/out/label.txt \
   /Users/ajit/deep-text-recognition-benchmark/out_lmdb
   Note: Replace the repository name with your own repo. Out is the loaction of data and labels.txt should be inside out dir.
   
## 5.Download deep-text-recognition-benchmark

## 6.Install the dependencies in venv

## 7.Download the TPS-ResNet-BiLSTM-Attn.pth

## 8.Command to train the model
  python train.py \
  --train_data out_lmdb \
  --valid_data out_lmdb \
  --select_data "/" \
  --batch_ratio 1.0 \
  --Transformation TPS \
  --FeatureExtraction ResNet \
  --SequenceModeling BiLSTM \
  --Prediction Attn \
  --batch_size 2 \
  --data_filtering_off \
  --workers 0 \
  --batch_max_length 80 \
  --num_iter 10000 \
  --valInterval 500 \
  --saved_model TPS-ResNet-BiLSTM-Attn.pth \
  --FT \
  --character “ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإآىئؤة"

## 9.Command to check the output
  python demo.py \
  --Transformation TPS \
  --FeatureExtraction ResNet \
  --SequenceModeling BiLSTM \
  --Prediction Attn \
  --image_folder test \
  --saved_model saved_models/TPS-ResNet-BiLSTM-Attn-Seed1111/best_accuracy.pth \
 --character "ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإآىئؤة"
  


