#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
import os


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class toc_test(unittest.TestCase):
    def setUp(self):
        self.ci = os.getenv('OAS_EXTERNAL_ENV')
        if os.getenv('OAS_EXTERNAL_ENV') == None:
            self.wd = webdriver.Firefox()
        else:
            # from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
            # binary = FirefoxBinary('/usr/bin/firefox', log_file=sys.stdout)
            # binary.add_command_line_options('-headless')
            # self.wd = webdriver.Firefox(firefox_binary=binary)
            #self.wd = webdriver.PhantomJS()
            #self.wd.set_window_size(1120, 550)
            self.wd = webdriver.Remote(desired_capabilities={
                "browserName": "firefox",
                "platform": "LINUX",
            })
        self.wd.implicitly_wait(60)

    def open_sedes(self):
        success = True
        wd = self.wd

        # esta ABIERTA de manera predeterminada. Se cierra el acordeon para grupo sedes
        headerElement = wd.find_element_by_css_selector(
            "#toc-div>ul>li:nth-child(1) .collapsible-header")
        headerElement.click()
        time.sleep(1)
        # se abre de nuevo el acordeon para grupo sedes
        headerElement.click()
        time.sleep(1)
        display = wd.find_element_by_css_selector(
            "#toc-div>ul>li:nth-child(1) .collapsible-body").value_of_css_property("display")
        if display != "block":
            success = False
            print("No despliega el TOC")
        # enciende todas las capas del grupo sedes
        iElement = wd.find_element_by_css_selector(
            "#toc-div a[data-group-layer-on='sedes'] i")
        iElement.click()
        time.sleep(1)
        # apaga todas las capas del grupo sedes DEJA apagado TODO
        iElement = wd.find_element_by_css_selector(
            "#toc-div a[data-group-layer-off='sedes'] i")
        iElement.click()
        time.sleep(1)
        # conmuta la capa construcción de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='construccion']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible construccion")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible construccion")
        # conmuta la capa nivel de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='nivel']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible nivel")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible nivel")
        # conmuta la capa sede punto de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='sede_punto']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible sede_punto")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
        # conmuta la capa zonas exteriores de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='zonas_exteriores']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible zonas_exteriores")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible zonas_exteriores")

        return success

    def open_arquitectonica(self):
        success = True
        wd = self.wd

        # Acordeon para grupo arquitectonica
        headerElement = wd.find_element_by_css_selector(
            "#toc-div>ul>li:nth-child(2) .collapsible-header")
        # se abre el acordeon para grupo arquitectonica
        headerElement.click()
        time.sleep(1)
        display = wd.find_element_by_css_selector(
            "#toc-div>ul>li:nth-child(2) .collapsible-body").value_of_css_property("display")
        if display != "block":
            success = False
            print("No despliega el TOC")
        # enciende todas las capas del grupo arquitectonica
        iElement = wd.find_element_by_css_selector(
            "#toc-div a[data-group-layer-on='arquitectonica'] i")
        iElement.click()
        time.sleep(1)
        # apaga todas las capas del grupo arquitectonica DEJA apagado TODO
        iElement = wd.find_element_by_css_selector(
            "#toc-div a[data-group-layer-off='arquitectonica'] i")
        iElement.click()
        time.sleep(1)
        # conmuta la capa espacio_fisico de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='espacio_fisico']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible espacio_fisico")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible espacio_fisico")

        return success

    def open_urbano(self):
        success = True
        wd = self.wd

        # Acordeon para grupo urbano
        headerElement = wd.find_element_by_css_selector(
            "#toc-div>ul>li:nth-child(3) .collapsible-header")
        # se abre el acordeon para grupo urbano
        headerElement.click()
        time.sleep(1)
        display = wd.find_element_by_css_selector(
            "#toc-div>ul>li:nth-child(3) .collapsible-body").value_of_css_property("display")
        if display != "block":
            success = False
            print("No despliega el TOC")
        # enciende todas las capas del grupo urbano
        iElement = wd.find_element_by_css_selector(
            "#toc-div a[data-group-layer-on='urbano'] i")
        iElement.click()
        time.sleep(1)
        # apaga todas las capas del grupo urbano DEJA apagado TODO
        iElement = wd.find_element_by_css_selector(
            "#toc-div a[data-group-layer-off='urbano'] i")
        iElement.click()
        time.sleep(1)
        # conmuta la capa ideca2 de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='ideca2']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible ideca2")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible ideca2")

        # conmuta la capa ideca de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='ideca']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible ideca")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible ideca")

        # conmuta la capa localidades_bogota de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='localidades_bogota']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible localidades_bogota")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible localidades_bogota")

        # conmuta la capa lote de la predeterminada a la contraria (on-off/off-on)
        iElement = wd.find_element_by_css_selector(
            "#toc-div i[data-layer-icon='lote']")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility":
            success = False
            print("No esta visible lote")
        iElement.click()
        time.sleep(1)
        if iElement.text != "visibility_off":
            success = False
            print("No esta invisible lote")

        return success

    def test_toc_test(self):
        success = True
        wd = self.wd
        wd.get("http://sig.udistrital.edu.co/")
        print("Esperando a que cargue visor...")
        time.sleep(10)  # seconds

        if not ("subject" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)

        # accede al menu lateral TOC (table of contents)
        wd.find_element_by_css_selector("a[href='#toc']").click()
        time.sleep(1)

        success = self.open_sedes()
        self.assertTrue(success)

        success = self.open_arquitectonica()
        self.assertTrue(success)

        success = self.open_urbano()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.close()


if __name__ == '__main__':
    unittest.main()
