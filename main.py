import numpy as np
import numpy.typing as npt
from scipy.special import expit as sigmoid


class NeuralNetwork:
    """
    Neural Network class, which can be trained and queried.
    """
    def __init__(self, input_nodes: int, hidden_nodes: int, output_nodes: int, learning_rate: float):
        ...

    def train(self, inputs_list: npt.NDArray[np.float64], targets_list: npt.NDArray[np.float64]) -> None:
        """
        Trains the neural network by adjusting the weights based on the inputs and targets.
        :param inputs_list: List of input values
        :param targets_list: List of target values
        """
        ...

    def query(self, inputs_list: npt.NDArray[np.float64]) -> np.ndarray:
        """
        Query the neural network with an input.
        :param inputs_list: List of input values
        :return: Output from the neural network
        """
        ...


def main() -> None:
    """
    Main function / Entry point of the program.
    """
    print('-- Manual Neural Network (DSAI class) -- ')


if __name__ == '__main__':
    main()
