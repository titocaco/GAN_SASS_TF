# GAN_SASS_TF
TensorFlow implementation of "GAN Single Audio Source Separation"

### WORK IN PROGRESS

To quickly train the model, modify `app/hparams.py` file to setup hyperparameter,
then run `python main.py -o saves/my_model.cpkt`.

This will will save model parameters in `saves/my_model.cpkt`

To continue training, run `python main.py -i saves/my_model.cpkt`

To check model accuracy on test set, do `python main.py -i <YOUR_MODEL_PARAMETERS> -m=test`

For more parameters help, do `python main.py --help`

The model currently has performance issues, and probably doesn't perform the task well ... yet.
