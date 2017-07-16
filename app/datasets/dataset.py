import numpy as np

import app.hparams as hparams


class Dataset(object):
    def __init__(self):
        self.is_loaded = False

    def epoch(self, subset, batch_size):
        '''
        Iterator, yields batches of numpy array
        Args:
            subset: string
            batch_size: int

        Yields:
            (signals, texts)
        '''
        raise NotImplementedError()

    def install_and_load(self):
        '''
        Download and preprocess dataset and store it on local disk.
        This method should check whether data is available in ./datasets,
        or already downloaded in ./downloads

        Raises:
            raise RuntimeError is something fails
        '''
        raise NotImplementedError()

@hparams.register_dataset('toy')
class WhiteNoiseData(object):
    '''
    this always generates uniform noise

    for signal, it's of length 128
    for text, it's of length 64
    '''
    # make it more general, support more shape
    def __init__(self):
        self.is_loaded = False

    def epoch(self, subset, batch_size):
        for _ in range(10):
            signal = np.random.rand(
                batch_size,
                hparams.MAX_N_SIGNAL,
                128,
                hparams.FFT_SIZE)
            text = np.random.randint(
                0, hparams.CHARSET_SIZE,
                (batch_size, hparams.MAX_N_SIGNAL, 64))
            yield signal, text

    def install_and_load(self):
        self.is_loaded = True
        return
