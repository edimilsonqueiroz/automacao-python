from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

## pip install webdriver-manager
## pip install selenium

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://app.powerbi.com')
sleep(5)
navegador.find_element('xpath','//*[@id="email"]').send_keys('targetbiitafarma2@targetsistemas.com.br')
sleep(5)
navegador.find_element('xpath','//*[@id="submitBtn"]').click()
sleep(5)
navegador.find_element('xpath','//*[@id="i0118"]').send_keys('Hug83020')
sleep(5)
navegador.find_element('xpath','//*[@id="idSIButton9"]').click()
sleep(5)
navegador.find_element('xpath','//*[@id="idSIButton9"]').click()
sleep(5)
navegador.find_element('xpath','//*[@id="content"]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/home/div/div[2]/div[1]/div/home-list-tab[2]/span').click()
sleep(5)
navegador.find_element('xpath','//*[@id="content"]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/home/div/div[2]/div[1]/tri-list-filter/div/tri-search-box/input').send_keys('LEG')
sleep(5)
navegador.find_element('xpath', '//*[@id="artifactContentView"]/div[2]/div/div[2]/div/span/a').click()
sleep(10)
navegador.find_element('xpath','//*[@id="content"]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/report/exploration-container/div/div/docking-container/div/div/exploration-fluent-navigation/section/nav/mat-action-list/button[1]/span').click()

sleep(60)

## //*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[1]/transform/div/visual-container-header/div/div/div/visual-container-options-menu/visual-header-item-container/div/button/i
## //*[@id="7"]/div/span
## //*[@id="mat-mdc-dialog-0"]/div/div/export-data-dialog/mat-dialog-actions/button[1]

## targetbiitafarma2@targetsistemas.com.br
## Hug83020