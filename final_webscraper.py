import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd


def scrape_products():
    final_df = pd.DataFrame(
        columns=['Name', 'Price', 'Condition', 'Category', 'Item no', 'EAN', 'Postage', 'Description',
                 'Image Url'])
    website_address = [
        'https://www.ebay.co.uk/itm/Edexcel-AS-A-level-history-Germany-and-West-Germany-1918-89-by-Barbara/293497601580?hash=item4455d1fe2c:g:6lYAAOSwbRFeXGqL',
        'https://www.ebay.co.uk/itm/South-Eastern-Chatham-Railway-album-by-P-K-Jones-Expertly-Refurbished-Product/293584629885?hash=item445b01f07d:g:omEAAOSwMWhfRSwP',
        'https://www.ebay.co.uk/itm/Watercolours-and-drawings-from-the-collection-of-Queen-Elizabeth-the-Queen/303516100277?hash=item46aaf826b5:g:DqkAAOSwQNNeb6NE',
        'https://www.ebay.co.uk/itm/The-Discworld-series-Carpe-jugulum-by-Terry-Pratchett-Paperback-Amazing-Value/293566021594?hash=item4459e5ffda:g:yssAAOSw3NBfQ7I0',
        'https://www.ebay.co.uk/itm/The-Bridge-On-the-River-Kwai-Das-Boot-The-Guns-of-Navarone-DVD-2006-Alec/301842143931?hash=item4647319abb:g:c3IAAOSwACRfPmfo',
        'https://www.ebay.co.uk/itm/Rio-Rio-2-DVD-2014-Carlos-Saldanha-cert-U-2-discs-Expertly-Refurbished-Product/381522751089?hash=item58d4872e71:g:8E0AAOSw84BfSMbi',
        'https://www.ebay.co.uk/itm/Death-Via-Satellite-CD-2005-Value-Guaranteed-from-eBay-s-biggest-seller/383630826477?hash=item59522ddbed:g:XvUAAOSw6BZfPm8A',
        'https://www.ebay.co.uk/itm/Dick-Gaughan-Redwood-Cathedral-CD-1998-Highly-Rated-eBay-Seller-Great-Prices/303098736580?hash=item469217afc4:g:eogAAOSwiWZfPXdw',
        'https://www.ebay.co.uk/itm/Sash-Best-of-Encore-une-fois-2000-15-tracks-CD-Expertly-Refurbished-Product/303589758408?hash=item46af5c15c8:g:cs0AAOSwlnhfPzdJ',
        'https://www.ebay.co.uk/itm/Various-Artists-Future-Bass-2014-CD-2-discs-2014-FREE-Shipping-Save-s/303623920885?hash=item46b1655cf5:g:eywAAOSwvyxfQmrz',
        'https://www.ebay.co.uk/itm/Ffh-Way-We-Worship-CD-Value-Guaranteed-from-eBay-s-biggest-seller/383633889951?hash=item59525c9a9f:g:DnwAAOSwAf5fR0Xu',
        'https://www.ebay.co.uk/itm/Murray-McLachlan-Piano-Music-CD-Value-Guaranteed-from-eBay-s-biggest-seller/293706427210?hash=item4462446b4a:g:QmUAAOSwofVfRv0e',
        'https://www.ebay.co.uk/itm/Berliner-Philarmoniker-The-Christmas-Album-Vol-2-CD-FREE-Shipping-Save-s/303565180823?hash=item46ade50f97:g:aOYAAOSw6atfPXHb',
        'https://www.ebay.co.uk/itm/The-etymologicon-a-circular-stroll-through-the-hidden-connections-of-the/383378956758?hash=item59432aa1d6:g:66AAAOSwm~BfRVPQ',
        'https://www.ebay.co.uk/itm/Disrupters-The-Generation-Retard-CD-Highly-Rated-eBay-Seller-Great-Prices/303587290533?hash=item46af366da5:g:-VIAAAzyWiRSwmIT',
        'https://www.ebay.co.uk/itm/Disrupters-The-Generation-Retard-CD-Highly-Rated-eBay-Seller-Great-Prices/303587290533?hash=item46af366da5:g:-VIAAAzyWiRSwmIT',
        'https://www.ebay.co.uk/itm/Blitzkrieg-myth-reality-and-Hitlers-lightning-war-France-1940-by-Lloyd/383430083433?hash=item594636c369:g:wOQAAOSwlGxfJBUD',
        'https://www.ebay.co.uk/itm/Lightnin-Hopkins-Masters-CD-Value-Guaranteed-from-eBay-s-biggest-seller/301811996020?hash=item4645659574:g:858AAOSw7ixfQL9j',
        'https://www.ebay.co.uk/itm/The-Bee-Gees-Ever-Increasing-Circles-CD-1993-Expertly-Refurbished-Product/293483858385?hash=item44550049d1:g:wg0AAOSwqDJfPq2d',
        'https://www.ebay.co.uk/itm/La-Fabulosa-Guitarra-De-european-Import-CD-1999-FREE-Shipping-Save-s/383204768691?hash=item5938c8bbb3:g:6~kAAOSwqY5fP4W0',
        'https://www.ebay.co.uk/itm/Orphans-of-the-storm-by-Katie-Flynn-Hardback-Expertly-Refurbished-Product/293687961503?hash=item44612aa79f:g:ussAAOSw5Z9fNg2N',
        'https://www.ebay.co.uk/itm/Dizzy-Gillespie-Diz-and-Getz-CD-2001-Highly-Rated-eBay-Seller-Great-Prices/303468813090?hash=item46a8269b22:g:q1kAAOSwksRfPv7y',
        'https://www.ebay.co.uk/itm/American-Bandstand-CD-2005-Value-Guaranteed-from-eBay-s-biggest-seller/383515832999?hash=item594b5332a7:g:wzwAAOSwbyFfP~rv',
        'https://www.ebay.co.uk/itm/No-off-switch-by-Andy-Kershaw-Paperback-softback-FREE-Shipping-Save-s/383511418346?hash=item594b0fd5ea:g:XEoAAOSwz5penV0a',
        'https://www.ebay.co.uk/itm/Something-Special-Laugh-With-Mr-Tumble-DVD-2017-Justin-Fletcher-cert-U/292654387120?hash=item44238f8fb0:g:3TsAAOSwKnlfRnFC',
        'https://www.ebay.co.uk/itm/The-Escorts-DVD-2017-Lisa-Addario-cert-TBC-Incredible-Value-and-Free-Shipping/293411599716?hash=item4450b1b564:g:08IAAOSw4jlfNON4',
        'https://www.ebay.co.uk/itm/21st-century-hotel-by-Graham-Vickers-Hardback-Expertly-Refurbished-Product/303568094320?hash=item46ae118470:g:cvwAAOSwRtBevhEn',
        'https://www.ebay.co.uk/itm/Aron-Paul-Founding-Feuds-The-Rivalries-Clashes-FREE-Shipping-Save-s/303599710236?hash=item46aff3f01c:g:g3gAAOSwlEZe6z9L',
        'https://www.ebay.co.uk/itm/Sheppard-Rob-Epson-Complete-Guide-to-Digital-Printing-FREE-Shipping-Save-s/303618865628?hash=item46b11839dc:g:gq0AAOSw5d5fSZuT',
        'https://www.ebay.co.uk/itm/Heart-of-Gold-by-J-R-Ward-Paperback-softback-Expertly-Refurbished-Product/293569940980?hash=item445a21cdf4:g:H3AAAOSwLAlfRVbX',
        'https://www.ebay.co.uk/itm/The-dream-book-dream-spells-night-time-potions-and-rituals-and-other-magical/383546372923?hash=item594d25333b:g:LMEAAOSwiKpfRndo',
        'https://www.ebay.co.uk/itm/Bournemouth-Symphony-Orchestra-Of-Beauty-and-Light-The-Music-Of-Alsop-CD-3/383571081360?hash=item594e9e3890:g:LiYAAOSwPqFfQByL',
        'https://www.ebay.co.uk/itm/Various-Artists-Son-Cubano-Nyc-CD-2005-Highly-Rated-eBay-Seller-Great-Prices/383518033549?hash=item594b74c68d:g:TLUAAOSwWg5fPqlK',
        'https://www.ebay.co.uk/itm/Stevan-Kovacs-Tickmayer-Repetitive-Selective-Removal-of-One-Protecting-Group/293571149185?hash=item445a343d81:g:pYUAAOSwq9BfQWiA',
        'https://www.ebay.co.uk/itm/Alpaca-chatter-by-Sue-Thomas-Merida-Woodford-Paperback-FREE-Shipping-Save-s/293664241445?hash=item445fc0b725:g:akkAAOSwSaNfRm6r',
        'https://www.ebay.co.uk/itm/Classic-Choral-Works-Messiah-Vocal-score-by-George-Frideric-Handel-Sheet/383551219248?hash=item594d6f2630:g:Mw0AAOSwun9ewkoJ',
        'https://www.ebay.co.uk/itm/Peter-Pan-and-Wendy-J-M-Barrie-by-J-M-Barrie-Robert-Ingpen-England-Hospital/383424048095?hash=item5945daabdf:g:5UkAAOSwIqpeSUYj',
        'https://www.ebay.co.uk/itm/Make-love-the-Bruce-Campbell-way-by-Bruce-Campbell-Paperback-Amazing-Value/303334744955?hash=item46a028e37b:g:HjwAAOSwArNfQ8E9',
        'https://www.ebay.co.uk/itm/Andre-Rieu-Andre-Rieu-Classics-from-Vienna-CD-2-discs-2012-Amazing-Value/383584360264?hash=item594f68d748:g:pbsAAOSw6dhfQ-MP',
        'https://www.ebay.co.uk/itm/Mistaken-identity-by-Lisa-Scottoline-Highly-Rated-eBay-Seller-Great-Prices/303610339244?hash=item46b0961fac:g:fLUAAOSwW5Je-1~X',
        'https://www.ebay.co.uk/itm/Around-Jarrow-by-John-Carlson-Paperback-softback-FREE-Shipping-Save-s/383618926847?hash=item59517848ff:g:K4kAAOSwwTtfAd8~',
        'https://www.ebay.co.uk/itm/Fishing-lures-by-Michael-Veale-Value-Guaranteed-from-eBay-s-biggest-seller/293642659860?hash=item445e776814:g:yJwAAOSwDPRfSGXN',
        'https://www.ebay.co.uk/itm/Barber-of-Seville-Romero-Hungarian-Radio-Choir-CD-3-discs-1994-Great-Value/303547128228?hash=item46acd199a4:g:5TUAAOSwW8RbEYG6',
        'https://www.ebay.co.uk/itm/Images-of-Wales-Grangetown-the-second-selection-by-Ian-Clarke-Amazing-Value/383627128702?hash=item5951f56f7e:g:7mgAAOSwkl5fRF~c',
        'https://www.ebay.co.uk/itm/Delius-Collection-Vol-7-CD-1999-Value-Guaranteed-from-eBay-s-biggest-seller/383555851560?hash=item594db5d528:g:PBYAAOSwfp9bEX-P',
        'https://www.ebay.co.uk/itm/Gathering-The-The-May-Song-CD-Value-Guaranteed-from-eBay-s-biggest-seller/293548529253?hash=item4458db1665:g:0QcAAOSwUlxfQ0G6',
        'https://www.ebay.co.uk/itm/A-Bernie-Gunther-novel-The-Prague-fatale-by-Philip-Kerr-Hardback-Great-Value/383452882490?hash=item594792a63a:g:RZMAAOSwDkJfRrif',
        'https://www.ebay.co.uk/itm/Oxford-worlds-classics-Adam-Bede-by-George-Eliot-Paperback-softback/303522317805?hash=item46ab5705ed:g:OWoAAOSw5BVeeVFy',
        'https://www.ebay.co.uk/itm/Easy-reading-Shakespeare-the-bard-in-bite-size-verse-by-Richard-Cuddington/293637527145?hash=item445e291669:g:PqkAAOSw6DVfAdWf',
        'https://www.ebay.co.uk/itm/Buckley-Betty-Heart-to-Heart-CD-Value-Guaranteed-from-eBay-s-biggest-seller/293550036099?hash=item4458f21483:g:-VQAAOSwkjtbEWkY',
        'https://www.ebay.co.uk/itm/Various-I-Am-Sam-CD-Value-Guaranteed-from-eBay-s-biggest-seller/303535239283?hash=item46ac1c3073:g:NSwAAOSwDvlfPqHO',
        'https://www.ebay.co.uk/itm/Little-Ticktock-What-am-I-animal-mums-and-babies-Hardback-Amazing-Value/303635345889?hash=item46b213b1e1:g:1LMAAOSwWuxfH8f9',
        'https://www.ebay.co.uk/itm/DELETED-SINATRA-FRANK-Mamselle-CD-Value-Guaranteed-from-eBay-s-biggest-seller/383506306816?hash=item594ac1d700:g:qBQAAOSwfZtbEXIE',
        'https://www.ebay.co.uk/itm/Addison-Wesley-professional-computing-series-Firewalls-and-Internet-security/303600416897?hash=item46affeb881:g:I6QAAOSwyANfR40a',
        'https://www.ebay.co.uk/itm/Jane-Olivor-Love-Decides-CD-Value-Guaranteed-from-eBay-s-biggest-seller/293461867713?hash=item4453b0bcc1:g:S3oAAOSwOxBfPi1R',
        'https://www.ebay.co.uk/itm/Leela-James-A-Change-Is-Gonna-Come-CD-2005-Expertly-Refurbished-Product/303520909761?hash=item46ab4189c1:g:VAsAAOSwjFVfPexJ',
        'https://www.ebay.co.uk/itm/Various-Polystar-Records-Legends-of-Hip-Hop-CD-Expertly-Refurbished-Product/303549072400?hash=item46acef4410:g:A4IAAOSw095fPdqz',
        'https://www.ebay.co.uk/itm/Various-Artists-Flower-Power-Lets-Go-to-San-Francisco-CD-2-discs-2004/303542693496?hash=item46ac8dee78:g:eD8AAOSwz7FfPU1J',
        'https://www.ebay.co.uk/itm/Civil-litigation-by-Inns-of-Court-School-of-Law-Paperback-softback/293574170657?hash=item445a625821:g:~KEAAOSwENVfSln8',
        'https://www.ebay.co.uk/itm/Digitally-Organic-An-Earlyworks-Press-P-Highly-Rated-eBay-Seller-Great-Prices/303626518396?hash=item46b18cff7c:g:AIQAAOSwdPRfEiUh',
        'https://www.ebay.co.uk/itm/Les-Fous-du-mercredi-BAY-TOM-NANA-Value-Guaranteed-from-eBay-s-biggest-seller/303658669157?hash=item46b3779465:g:XqQAAOSw4qxfPGPk',
        'https://www.ebay.co.uk/itm/Great-battles-Corunna-by-Christopher-Hibbert-Paperback-softback-Great-Value/303627665320?hash=item46b19e7fa8:g:6TwAAOSwMwZfFCos',
        'https://www.ebay.co.uk/itm/Various-Artists-Pure-Guitar-Moods-CD-4-discs-2004-FREE-Shipping-Save-s/303612703679?hash=item46b0ba33bf:g:cckAAOSwFNZfPXjB',
        'https://www.ebay.co.uk/itm/Research-methods-in-clinical-psychology-an-introduction-for-students-and/303367359517?hash=item46a21a8c1d:g:9QwAAOSwy91fHhik',
        'https://www.ebay.co.uk/itm/Murderous-maths-The-murderous-maths-of-everything-by-Kjartan-Poskitt/382295819477?hash=item59029b44d5:g:LKUAAOSwy8JdgKrN',
        'https://www.ebay.co.uk/itm/Ochre-Room-Evening-Coming-in-CD-Value-Guaranteed-from-eBay-s-biggest-seller/383509981748?hash=item594af9ea34:g:CmYAAOSwW2tem-Jx',
        'https://www.ebay.co.uk/itm/Frankie-says-relapse-by-Siobhan-Curham-Paperback-softback-Quality-guaranteed/293669772460?hash=item4460151cac:g:~3YAAOSwS91fRk3C',
        'https://www.ebay.co.uk/itm/Zentangle-the-inspiring-and-mindful-drawing-method-by-Jane-Marbaix-Paperback/383574730917?hash=item594ed5e8a5:g:sIsAAOSwIftfQ-hC',
        'https://www.ebay.co.uk/itm/Lukas-Klansky-Piano-Forte-The-Next-Generation-CD-2-discs-2017-Amazing-Value/293548121163?hash=item4458d4dc4b:g:27AAAOSwJQBfSi2O',
        'https://www.ebay.co.uk/itm/Modules-in-environmental-science-Environmental-economics-a-critical-overview/293705649222?hash=item4462388c46:g:2rEAAOSwCr5fRTc3',
        'https://www.ebay.co.uk/itm/THE-GARDENERS-PLANNING-BOX-by-PETER-MCHOY-Hardback-FREE-Shipping-Save-s/303625285829?hash=item46b17a30c5:g:N5kAAOSwiBNfEHFI',
        'https://www.ebay.co.uk/itm/The-liquid-enterprise-How-the-network-is-transforming-value-what-it-means-for/293654741560?hash=item445f2fc238:g:2qAAAOSwPSBfFW9B',
        'https://www.ebay.co.uk/itm/Romans-Saxons-Vikings-Beliefs-and-myths-of-Viking-Britain-by-Martyn-J/383529011265?hash=item594c1c4841:g:kWsAAOSwmgJe1DBr',
        'https://www.ebay.co.uk/itm/Various-Artists-They-Do-It-With-Mirrors-Complete-Unab-CD-Quality-guaranteed/383571628927?hash=item594ea6937f:g:XLQAAOSwFtFfQTJ']
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    for web in website_address:
        browser.get(web)
        time.sleep(2)

        time.sleep(5)
        product_price_raw_list = browser.find_element_by_xpath('//*[@id="vi-mskumap-none"]').text
        product_name_raw_lst = browser.find_element_by_xpath('//*[@id="itemTitle"]').text
        product_condition = browser.find_element_by_xpath('//*[@id="vi-itm-cond"]').text
        product_category = browser.find_element_by_xpath('//*[@id="vi-VR-brumb-lnkLst"]/table/tbody/tr/td/ul/li[1]').text
        product_ebay_item_no = browser.find_element_by_xpath('//*[@id="descItemNumber"]').text
        product_ean = browser.find_element_by_xpath('//*[@id="viTabs_0_is"]/div/table[2]/tbody/tr/td[2]').text
        product_postage = browser.find_element_by_xpath('//*[@id="shSummary"]').text
        # product_rrp = browser.find_element_by_xpath('//*[@id="vi-priceDetails"]/span[1]/span[2]/span').text
        # product_about = browser.find_element_by_xpath('//*[@id="viTabs_0_pd"]/div/table/tbody').text
        product_desc = browser.find_element_by_xpath('//*[@id="viTabs_0_is"]').text
        product_image_url = browser.find_element_by_xpath('//*[@id="icImg"]')
        image_url = product_image_url.get_attribute('src')
        print(image_url)

        data_frame = pd.DataFrame([[product_name_raw_lst, product_price_raw_list, product_condition, product_category,
                                    product_ebay_item_no, product_ean, product_postage,
                                    product_desc, image_url]],
                                  columns=['Name', 'Price', 'Condition', 'Category', 'Item no', 'EAN', 'Postage',
                                           'Description', 'Image Url'])
        final_df = final_df.append(data_frame, ignore_index=True)
    final_df.to_csv('crawler_ebay_3.csv', index=False)
    print(final_df.head())
    print('ITS DONE!!')


if __name__ == "__main__":
    scrape_products()
