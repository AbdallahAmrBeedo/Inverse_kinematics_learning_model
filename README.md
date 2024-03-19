# Inverse Kineamtics Learning Model for 2 Link Manipulator
ANN model fitted on a data from a 2 link manipulator forward kineamtics to drive the inverse kinematics of the manipulator and test it on a simulated and visualized model.

## Install

### Dependencies
- numpy
- pandas
- matplotlib
- livelossplot
- scikit-learn
- tensorflow

```bash
git clone https://github.com/AbdallahAmrBeedo/Inverse_kinematics_learning_model.git

cd Inverse_kinematics_learning_model/

chmod a+x install_dep.sh

./install_dep.sh

```

## Tutorial

### Dataset Generation
to generate the dataset for the manipulator, run
```bash
python3 gen_data_set.py
```
A csv will be created in ```/data``` directory with 40000.

