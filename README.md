## Programmation parallèle pour le *Machine Learning*

Ce projet a été réalisé dans le cadre du cours "Programmation parallèle pour le *Machine Learning*", dispensé par Xavier Dupré et Matthieu Durut à l'ENSAE Paris. Il porte sur la parallélisation sur CPU d'une séquence d'opérations matricielles extraites d'un modèle Llama. Plus précisément, à partir d'une matrice `A`, il s'agit de paralléliser la séquence d'opérations `sigmoid(A) * A` en C++, et de comparer les performances de cette méthode à son équivalent non parallélisé codé en `torch`. 

## Accès au code

Tout d'abord, clonez le dépôt:
```bash
git clone https://github.com/matthieu-bricaire/parallel-programming-ensae.git
```

Si vous utilisez conda, créez un nouvel environnement :
```bash
conda create -n env_name python==3.12.2
```

Puis, installez-y les *requirements*:
```bash
pip install -r requirements.txt
```

## Contenu du dépôt

### Création de l'extension et utilisation
Ce dépôt contient les codes nécessaires à la création d'une extension Python (`sigmulib`), basée sur des fonctions codées en C++ qui parallélisent la séquence d'opérations `sigmoid(A) * A`:

- `sigmul.cpp` : version C++ de `sigmoid(A) * A`.
- `interface.pyx` : version Cython de `sigmoid(A) * A`, et déclaration en Cython de la version C++ basée sur `sigmul.cpp`
- `setup.py` : code relatif à la création de l'extension

Pour créer l'extension, il suffit d'exécuter la commande suivante :
```python
python setup.py build_ext --inplace
```

Cette commande crée :
- Un fichier `interface.cpp` (correspondant au fichier `interface.pyx`)
- Un dossier `build/`, contenant des fichiers spécifiques liés à l'extension construite
- Le fichier `sigmulib.cpython-312-x86_64-linux-gnu.so`, qui correspond à l'extension qui sera appelée en python.

Une fois l'extension construite, elle peut être importée et utilisée en python avec la commande `import sigmulib`.

### Analyses
Ce dépôt contient également les codes associés aux expériences et aux analyses menées:

- `times_comparisons.ipynb` : comparaison des performances des différentes stratégies
- `utils.py` : regroupement de fonctions utilisées lors des analyses