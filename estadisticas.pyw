#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#Importar aquí las librerías a utilizar
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro
import pylab 
import scipy.stats as stats
import seaborn as sns
import statsmodels as sm
import statsmodels.api as sms
from patsy import dmatrices
from PyQt5 import uic, QtWidgets

qtCreatorFile = "estadisticas.ui" #Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("EstadisticasApp")
        
        #Aquí van los botones
        self.boton1.clicked.connect(self.getCSV)
        self.boton2.clicked.connect(self.shapiro)
        self.boton3.clicked.connect(self.jarque)
        self.boton4.clicked.connect(self.estadisticasb)
        self.boton6.clicked.connect(self.lineal)
        self.boton5.clicked.connect(self.gresumen)
        self.boton7.clicked.connect(self.head)
        self.boton8.clicked.connect(self.limpiar)
        self.boton9.clicked.connect(self.kolmogorov)
        self.boton10.clicked.connect(self.chi)
        self.boton11.clicked.connect(self.lillie)
        self.boton12.clicked.connect(self.varianzas)
        self.botont.clicked.connect(self.tmedia)
        self.botonm.clicked.connect(self.mannw)
        self.botonpie.clicked.connect(self.pie)
        self.barras.clicked.connect(self.bar)
        self.Excel.clicked.connect(self.getEXCEL)
        self.corr.clicked.connect(self.cor)


    #Aquí van las nuevas funciones
    #Esta función abre el archivo CSV



    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath))
            self.cb1.addItems(list(self.df.columns.values))
            self.cb2.addItems(list(self.df.columns.values))
            self.cb3.addItems(list(self.df.columns.values))
            self.cb4.addItems(list(self.df.columns.values))
            self.cb5.addItems(list(self.df.columns.values))

    def getEXCEL(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
            self.df = pd.read_excel(str(filePath))
            self.cb1.addItems(list(self.df.columns.values))
            self.cb2.addItems(list(self.df.columns.values))
            self.cb3.addItems(list(self.df.columns.values))
            self.cb4.addItems(list(self.df.columns.values))
            self.cb5.addItems(list(self.df.columns.values))

    def lineal(self):
        x=self.df[str(self.cb1.currentText())]
        stats.probplot(x, dist="norm", plot=pylab)
        pylab.show()
        

    def gresumen(self):
        x=self.df[str(self.cb2.currentText())]
        sns.distplot(x)
        plt.show()
        

    def limpiar(self):
        self.cb1.clear()
        self.cb2.clear()
        self.cb3.clear()
        self.cb4.clear()
        self.cb5.clear()


    def head(self):

        a=self.df[self.cb3.currentText()]
        b=pd.DataFrame(a)
        estad_st='Nombre de las variables: '+'\n'+str(self.df.columns.tolist())+'\n'+str(self.cb3.currentText())+': informacion columnas y filas:  '+'\n'+str(self.df.head())
        self.resultado.setText(estad_st)
        plt.boxplot(a)
        #self.df.drop([str(self.cb3.currentText())],1).hist()
        self.df.drop(columns=[str(self.cb3.currentText())]).hist()
        plt.show()
        

    def pie (self):
        a=self.df[self.cb3.currentText()]
        colors = sns.color_palette('pastel')
        plt.pie(a, colors = colors)
        plt.show()

    def cor (self):
        # Calcular la matriz de correlación
        corr_matrix = self.df.corr()
        # Crear el mapa de correlación utilizando Seaborn
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        # Ajustar el aspecto del mapa de correlación
        plt.title('Mapa de Correlación')
        plt.show()
        
 
    def shapiro (self):
        a=self.df[self.cb3.currentText()]
        h=shapiro(a)
        estadistico, p_value= shapiro(a)##Shapiro-Wilk
        estad_st='Prueba Shapiro-Wilk:  '+'\n'+str(self.cb3.currentText())+str(h)+'\n'+str(' Datos resumidos y aproximados: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))
        self.resultado.setText(estad_st)


    def jarque (self):
        c=self.df[self.cb3.currentText()]
        j = stats.jarque_bera(c)
        estadistico, p_value = stats.jarque_bera(c)
        estad_st='prueba jarque bera: '+'\n'+str(self.cb3.currentText())+str(j)+'\n'+str(
            ' Datos resumidos y aproximados: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))
        self.resultado.setText(estad_st)

    def kolmogorov(self):
        k=self.df[self.cb3.currentText()]
        s=stats.kstest(k, 'norm')
        estadistico, p_value=stats.kstest(k, 'norm')
        estad_st='prueba Kolmogorov-Smirnov: '+'\n'+str(self.cb3.currentText())+str(s)+'\n'+str(' Datos resumidos y aproximados: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))
        self.resultado.setText(estad_st)

    def chi(self):
        from scipy.stats import chisquare
        l=self.df[self.cb3.currentText()]
        ch=stats.chisquare(l)
        estadistico, p_value = chisquare(l, ddof=0)
        estad_st='Prueba chi cuadrado test:  '+'\n'+str(self.cb3.currentText())+str(ch)+'\n'+str(' Datos resumidos y aproximados: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))
        self.resultado.setText(estad_st)

    def lillie(self):
        ll=self.df[self.cb3.currentText()] 
        li=sm.stats.diagnostic.lilliefors(ll, dist='norm')
        estadistico, p_value=sm.stats.diagnostic.lilliefors(ll, dist='norm')
        estad_st='Prueba Lilliefors’ test:  '+'\n'+str(self.cb3.currentText())+str(li)+'\n'+str(' Datos resumidos y aproximados: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))
        self.resultado.setText(estad_st)

    def bar (self):
        x1=self.df[self.cb4.currentText()] 
        y1=self.df[self.cb5.currentText()]
        sns.set(style='whitegrid')
        plt.figure(figsize=(8, 6))
        sns.barplot(x=x1, y=y1)
        plt.show()

    def varianzas(self):
    	var1=self.df[self.cb4.currentText()] 
    	var2=self.df[self.cb5.currentText()] 
    	va=stats.levene(var1,var2)
    	estadistico, p_value = stats.levene(var1,var2)
    	estad_st='Prueba de Levene para varianzas iguales:  '+'\n'+str(self.cb4.currentText())+'\n'+str(self.cb5.currentText())+str(va)+'\n'+str(' Datos resumidos y aproximados: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))
    	self.resultado.setText(estad_st)
    def tmedia(self):
        t1=self.df[self.cb4.currentText()]
        t2=self.df[self.cb5.currentText()] 
        tm=stats.ttest_ind(t1,t2, equal_var = True)
        estadistico, p_value = stats.ttest_ind(t1,t2, equal_var = True)
        estadistico1, p_value1 = stats.ttest_ind(t1,t2, equal_var = False)
        estad_st='Prueba T-student independientes:  '+'\n'+str(self.cb5.currentText())+str(tm)+'\n'+str('Varianzas iguales: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))+'\n'+str('Varianzas diferentes: estadistico=%.4f, p_value=%.4f' % (estadistico1, p_value1))
        self.resultado.setText(estad_st)

    def mannw(self):
        w=self.df[self.cb4.currentText()]
        m=self.df[self.cb5.currentText()]
        estadistico, p_value = stats.mannwhitneyu(w,m,alternative='less')
        estadistico1, p_value1 = stats.mannwhitneyu(w,m, alternative='greater')
        estadistico2, p_value2 = stats.mannwhitneyu(w,m, alternative='two-sided')
        estad_st='Prueba de Mann-Whitney en las muestras:  '+'\n'+str('Cola izquierda: estadistico=%.4f, p_value=%.4f' % (estadistico, p_value))+'\n'+str('Cola derecha: estadistico=%.4f, p_value=%.4f' % (estadistico1, p_value1))+'\n'+str('Dos colas: estadistico=%.4f, p_value=%.4f' % (estadistico2, p_value2))
        self.resultado.setText(estad_st)


    def estadisticasb (self):
        
        estad_st='Estadisticas basicas:  '+'\n'+str(self.cb3.currentText())+str(self.df[self.cb3.currentText()].describe(include='all'))
        self.resultado.setText(estad_st)

        

    
    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
