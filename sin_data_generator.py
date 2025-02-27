import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from sklearn import preprocessing

def normalize(arr, t_min=0, t_max=1):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = np.max(arr) - np.min(arr)    
    for i in arr:
        temp = (((i - np.min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr

"""
Generates data from a given sin function with added noise. Simulates the kind of periodic wave data
recorded from Grav Wave detectors such as LIGO.
    Parameters
    ----------
    snr : float
        The variance that is used on the gaussian to decided how much noise to add.
    freq : list, float
        Frequencies, a list of two values, [start frequency, last frequency]..
    length : int, optional
        Number of outputs generated. Limited by storage space of qubits.

    Raises
    ------
    Exception
        If labels generate incorrectly

    Returns
    -------
    list
        Returns generated data with accompanying labels for each set of data points

"""
def sin_gen(snr, freq, length):
    # Number of data points in each graph
    data_length = 256

    # Initalising lists for data point storage
    outputs = []
    labels = []

    for i in range(0, length):
        # Randomly decides if the data will be signal (1) or noise (0)
        label = np.random.randint(0,2)

        # Noise only signal generated via random sampling from a gaussian distribution
        if label == 0:
            x = np.linspace(0,0,data_length)
            labels.append(label)
            noise = np.random.normal(0, snr, data_length) # Generates random gaussian noise with sigma=snr
            output = x + noise
        
        # Signals generated by building a sin plot then adding randomly sampling from a gaussian distribution as noise
        elif label == 1:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency = np.random.randint(freq[0], freq[1])
            signal = np.sin((frequency * x))
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise

        else:
            raise Exception("Error encountered whilst producing sin plots. Should be impossible, check random label generator")
        
        output /= np.sqrt(np.sum(np.abs(output)**2))
        outputs.append(output)

    dataset = [outputs, labels]

    return dataset

"""
Generates data from a given sin functions of different frequencies with added noise. Simulates the kind of periodic wave data
recorded from Grav Wave detectors such as LIGO.
    Parameters
    ----------
    snr : float
        The variance that is used on the gaussian to decided how much noise to add.
    freq : list, float
        Frequencies, a list of two values, [start frequency, last frequency]..
    length : int, optional
        Number of outputs generated. Limited by storage space of qubits.

    Raises
    ------
    Exception
        If labels generate incorrectly

    Returns
    -------
    list
        Returns generated data with accompanying labels for each set of data points

"""
def multi_sin_gen(snr, freq_1, freq_2, freq_3, length):
    # Number of data points in each graph
    data_length = 256

    outputs = []
    labels = []

    for i in range(0, length):
        # Randomly decides if the data will be noise (0), signal with freq_1 (1), signal with freq_2 (2)
        label = np.random.randint(0,4)

        if label == 0:
            x = np.linspace(0,0,data_length)
            labels.append(label)
            noise = np.random.normal(0, snr, data_length) # Generates random gaussian noise with sigma=snr
            output = x + noise
        
        elif label == 1:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency = np.random.randint(freq_1[0], freq_1[1])
            signal = np.sin((frequency * x))
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise
        
        elif label == 2:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency = np.random.randint(freq_2[0], freq_2[1])
            signal = np.sin((frequency * x))
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise
        
        elif label == 3:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency = np.random.randint(freq_3[0], freq_3[1])
            signal = np.sin((frequency * x))
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise

        else:
            raise Exception("Error encountered whilst producing sin plots. Should be impossible, check random label generator")
        
        output /= np.sqrt(np.sum(np.abs(output)**2))
        outputs.append(output)

    dataset = [outputs, labels]

    return dataset

"""
Generates data from a given sin wave, superposition wave and time-varying frequency wave with added noise. Simulates the kind of periodic wave data
recorded from Grav Wave detectors such as LIGO.
    Parameters
    ----------
    snr : float
        The variance that is used on the gaussian to decided how much noise to add.
    freq : list, float
        Frequencies, a list of two values, [start frequency, last frequency]..
    length : int, optional
        Number of outputs generated. Limited by storage space of qubits.

    Raises
    ------
    Exception
        If labels generate incorrectly

    Returns
    -------
    list
        Returns generated data with accompanying labels for each set of data points

"""
def multi_plot_gen(snr, freq_1, freq_2, freq_3, length):
    
    # Number of data points in each graph
    data_length = 256

    outputs = []
    labels = []

    for i in range(0, length):
        # Randomly decides if the data will be noise (0), sinusoidal signal with freq_1 (1), combined sinusoidal signal with freq_2 (2),
        # and exponential signal with freq_3 (3)
        label = np.random.randint(0,4)

        if label == 0:
            if snr != 0:
                x = np.linspace(0,0,data_length)
                labels.append(label)
                noise = np.random.normal(0, snr, data_length) # Generates random gaussian noise with sigma=snr
                output = x + noise
            else:
                output = np.random.normal(0, 1, data_length)
                labels.append(label)
        
        elif label == 1:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency = np.random.randint(freq_1[0], freq_1[1])
            signal = np.sin((frequency * x))
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise
        
        elif label == 2:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency_1 = np.random.randint(freq_2[0], freq_2[1])
            frequency_2 = np.random.randint(freq_2[0], freq_2[1])
            signal = np.sin((frequency_1 * x)) + np.sin((frequency_2 * x))
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise

        elif label == 3:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency_1 = np.random.randint(freq_3[0], freq_3[1])
            frequency_2 = np.random.randint(freq_3[2], freq_3[3])
            signal = np.cos((frequency_1 * x + frequency_2 * x ** 2))
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise

        else:
            raise Exception("Error encountered whilst producing sin plots. Should be impossible, check random label generator")
        
        #output /= np.sqrt(np.sum(np.abs(output)**2))
        #output /= np.sqrt(np.sum(np.abs(output)**2))
        output = preprocessing.normalize([output], norm='l2')
        #if i < 10:
            #print(f"Sum of amplitudes-squared for output {i} and label {label}: {np.sum(np.abs(output)**2)}")
        #print(output[0])
        outputs.append(output[0])

    dataset = [outputs, labels]

    return dataset

"""
Generates data from a given time-varying frequency function of different frequency ranges with added noise. Simulates the kind of periodic wave data
recorded from Grav Wave detectors such as LIGO.
    Parameters
    ----------
    snr : float
        The variance that is used on the gaussian to decided how much noise to add.
    freq : list, float
        Frequencies, a list of two values, [start frequency, last frequency]..
    length : int, optional
        Number of outputs generated. Limited by storage space of qubits.

    Raises
    ------
    Exception
        If labels generate incorrectly

    Returns
    -------
    list
        Returns generated data with accompanying labels for each set of data points

"""
def multi_time_plot_gen(snr, freq_1, freq_2, freq_3, length):
    # Number of data points in each graph
    data_length = 256

    outputs = []
    labels = []

    for i in range(0, length):
        # Randomly decides if the data will be noise (0), sinusoidal signal with freq_1 (1), combined sinusoidal signal with freq_2 (2),
        # and exponential signal with freq_3 (3)
        label = np.random.randint(0,4)

        if label == 0:
            x = np.linspace(0,0,data_length)
            labels.append(label)
            noise = np.random.normal(0, snr, data_length) # Generates random gaussian noise with sigma=snr
            output = x + noise
        
        elif label == 1:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency_1 = np.random.randint(freq_1[0], freq_1[1])
            frequency_2 = np.random.randint(freq_1[2], freq_1[3])
            signal = np.cos(frequency_1 * x + frequency_2 * x ** 2)
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise
        
        elif label == 2:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency_1 = np.random.randint(freq_2[0], freq_2[1])
            frequency_2 = np.random.randint(freq_2[2], freq_2[3])
            signal = np.cos(frequency_1 * x + frequency_2 * x ** 2)
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise

        elif label == 3:
            x = np.linspace(0, 2*np.pi, data_length)
            labels.append(label)
            # Randomised Frequency of the sine wave
            frequency_1 = np.random.randint(freq_3[0], freq_3[1])
            frequency_2 = np.random.randint(freq_3[2], freq_3[3])
            signal = np.cos(frequency_1 * x + frequency_2 * x ** 2)
            noise = np.random.normal(0, snr, data_length)
            output = signal + noise

        else:
            raise Exception("Error encountered whilst producing sin plots. Should be impossible, check random label generator")
        
        output /= np.sqrt(np.sum(np.abs(output)**2))
        
        outputs.append(output)

    dataset = [outputs, labels]

    return dataset


# Testing data generation
if __name__ == "__main__":
    sin_gen(0.5, [10,30], 10)
    multi_sin_gen(0.5, [10, 30], [60, 80], 10)
    multi_plot_gen(0.5, [10, 30], [60, 80], [100, 120], 10)
    multi_time_plot_gen(0.5, [10, 30], [60, 80], [100, 120], 10)
