# python 3.5.2
import random, math

# //Indice:

# Descripcion:
"""Perceptron simple, capaz
de aprender patrones no lineales."""

class Neuron():
    def __init__(self, Input, LCP):
        # Input=Numero de entradas, LCP=Indice de aprendizaje
        self.Weight = [random.uniform(-1, 1) for n in range(Input)]  # Crea pesos aleatorios para cada entrada.
        self.Umbral = random.uniform(-1, 1)  # Crea un umbral aleatorio
        self.LastWeight = self.Weight  # Guarda los ultimos pesos
        self.LastUmbral = self.Umbral  # Guarda el ultimo umbral
        print("Pesos Iniciales: " + str(self.Weight))
        print("Umbral Inicial: " + str(self.Umbral))
        self.LCP = LCP  # Indice de aprendizaje.

    def Funtion(self, Input):
        RT = self.Umbral  # Añade el umbral
        for x in range(len(self.Weight)):
            RT += Input[x] * self.Weight[x]  # Suma los productos(Entrada*Peso)
        return RT;  # Retorna los resultados.

    def Sigmoide(self, x):
        return (1 / (1 + math.exp(-x)))  # Funcion Sigmoide(Version. Unipolar) // No es la misma del tuto

    def Output(self, Input):
        return self.Sigmoide(self.Funtion(Input));  # Devuelve el sigmoide de la sumatoria

    def Learn(self, Input, OutputA):
        if len(self.LastWeight) > 0:  # Verifica si tiene datos de los ultimos pesos
            Error = OutputA - self.Output(Input)  # Identifica el error
            for x in range(len(self.Weight)):
                self.Weight[x] = self.LastWeight[x] + self.LCP * Error * Input[x]  # Corrije el error de cada peso
            self.Umbral = self.LastUmbral + self.LCP * Error  # Corrije el error del umbral.
            self.LastWeight = self.Weight  # Guarda los ultimos pesos
            self.LastUmbral = self.Umbral  # Guarda el ultimo umbral
        else:
            self.LastWeight = self.Weight  # Guarda los ultimos pesos
            self.LastUmbral = self.Umbral  # Guarda el ultimo umbral


# //Datos
Nweb = Neuron(2, 0.3)  # Crea la neurona.
Exit = [1, 0, 0, 0]
Age = 25  # Numero de etapas maximas.


# \\
def Redon(Input):  # // Esta funcion solo convierte las  salidas de enteros binarios osea 1 o 0.
    dict = {
        True: 1,
        False: 0
    }
    return dict[Input > 0.5]


# //Loop principal.
for x in range(Age):
    Var = True  # Variable auxiliar
    print("\n>> Etapa: " + str(x + 1))
    print("Entrada '1,1': " + str(Nweb.Output((1, 1))) + "/" + str(Exit[0]) + "; Objetivo: " + str(
        Redon(Nweb.Output((1, 1)))))
    print("Entrada '1,0': " + str(Nweb.Output((1, 0))) + "/" + str(Exit[1]) + "; Objetivo: " + str(
        Redon(Nweb.Output((1, 0)))))
    print("Entrada '0,1': " + str(Nweb.Output((0, 1))) + "/" + str(Exit[2]) + "; Objetivo: " + str(
        Redon(Nweb.Output((0, 1)))))
    print("Entrada '0,0': " + str(Nweb.Output((0, 0))) + "/" + str(Exit[3]) + "; Objetivo: " + str(
        Redon(Nweb.Output((0, 0)))))

    # Revisa si comete un error
    if Redon(Nweb.Output((1, 1))) != Exit[0]:
        Nweb.Learn((1, 1), Exit[0])  # Aprende
        Var = False
    if Redon(Nweb.Output((1, 0))) != Exit[1]:
        Nweb.Learn((1, 0), Exit[1])  # Aprende
        Var = False
    if Redon(Nweb.Output((0, 1))) != Exit[2]:
        Nweb.Learn((0, 1), Exit[2])  # Aprende
        Var = False
    if Redon(Nweb.Output((0, 0))) != Exit[3]:
        Nweb.Learn((0, 0), Exit[3])  # Aprende
        Var = False

    if Var != False:  # Si no hubo error: Para el aprendizaje.
        print("<Datos Aprendidos>")
        break;
# \\