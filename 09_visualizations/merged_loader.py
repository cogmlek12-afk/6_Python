"""
    통합 데이터 로더
"""
from loader import load_prices, load_companies, load_sectors
def load_merged():
    """
        시세(prices) + 종목(companies) + 섹터(sectors) 반환
    """
    
    price = load_prices()
    companies = load_companies()
    sectors = load_sectors().rename(columns={"code":"sectorCode", "name":"sector"})

    df = (
        price
        .merge(companies[['code', 'name', 'sectorCode', 'market']],
               on='code', how='left', validate='many_to_one')
        .merge(sectors[['sectorCode', 'setor']],
               on = 'sectorCode', how='left', validate='many_to_one')

               
    )