# Fine tuning EasyOCR Model
## 1.Download the TextRecognitionDataGenerator
## 2.Install the dependencies in a virtual enviornment.
## 3.Use the following command to generate arabic dataset
trdg -l ar -c 1000 -w 1
## 4.Download deep-text-recognition-benchmark
## 5.Install the dependencies in venv
## 6.Download the TPS-ResNet-BiLSTM-Attn.pth
## 7.Command to train the model
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

## 8.Command to check the output
  python demo.py \
  --Transformation TPS \
  --FeatureExtraction ResNet \
  --SequenceModeling BiLSTM \
  --Prediction Attn \
  --image_folder test \
  --saved_model saved_models/TPS-ResNet-BiLSTM-Attn-Seed1111/best_accuracy.pth \
 --character "ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإآىئؤة"
  


