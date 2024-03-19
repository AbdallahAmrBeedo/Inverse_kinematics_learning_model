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
A csv will be created in ```/data``` directory with 6400 data points.

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
      <th>theta</th>
      <th>q1</th>
      <th>q2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.0000</td>
      <td>0.0000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.9974</td>
      <td>0.0715</td>
      <td>0.071581</td>
      <td>0.000000</td>
      <td>0.071581</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.9898</td>
      <td>0.1427</td>
      <td>0.143161</td>
      <td>0.000000</td>
      <td>0.143161</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.9770</td>
      <td>0.2131</td>
      <td>0.214742</td>
      <td>0.000000</td>
      <td>0.214742</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.9593</td>
      <td>0.2824</td>
      <td>0.286322</td>
      <td>0.000000</td>
      <td>0.286322</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6395</th>
      <td>0.8369</td>
      <td>-1.5874</td>
      <td>11.023411</td>
      <td>5.654867</td>
      <td>5.368544</td>
    </tr>
    <tr>
      <th>6396</th>
      <td>0.9083</td>
      <td>-1.5828</td>
      <td>11.094992</td>
      <td>5.654867</td>
      <td>5.440125</td>
    </tr>
    <tr>
      <th>6397</th>
      <td>0.9792</td>
      <td>-1.5732</td>
      <td>11.166572</td>
      <td>5.654867</td>
      <td>5.511706</td>
    </tr>
    <tr>
      <th>6398</th>
      <td>1.0492</td>
      <td>-1.5585</td>
      <td>11.238153</td>
      <td>5.654867</td>
      <td>5.583286</td>
    </tr>
    <tr>
      <th>6399</th>
      <td>1.1180</td>
      <td>-1.5388</td>
      <td>11.309734</td>
      <td>5.654867</td>
      <td>5.654867</td>
    </tr>
  </tbody>
</table>
<p>6400 rows × 5 columns</p>
</div>

### Trainning ANN Model

A model with 6 Hidden layers and 10272 trainable paramters in ```model_train.ipynb``` just run the cells to train, evaluate and save the model.

### Visualization

run
```bash
python3 inv_kinematic_viz.py
```
wait for the model to be loaded, enter x, y, theta you desire and the model will solve the inverse kinematics and plot the manipulator to verify.