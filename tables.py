# tables.py
calendar_table = """
 <table class="calendar">
    <tr>
        <th>Dom</th>
        <th>Lun</th>
        <th>Mar</th>
        <th>Mié</th>
        <th>Jue</th>
        <th>Vie</th>
        <th>Sáb</th>
        
        
    </tr>
    
    <tr>
        <td class="disabled"><span>30</span></td>
        <td class="disabled"><span>31</span></td>
        <td class="disabled"><span>1</span></td>
        <td class="disabled"><span>2</span></td>
        <td class="disabled"><span>3</span></td>
        <td class="disabled"><span>4</span></td>
        <td class="disabled"><span>5</span></td>
        
    </tr>

    <tr>
        <td class="disabled"><span>6</span></td>
        <td class="disabled"><span>7</span></td>
        <td class="disabled"><span>8</span></td>
        <td class="disabled"><span>9</span></td>
        <td class="disabled"><span>10</span></td>
        <td class="disabled"><span>11</span></td>
        <td class="disabled"><span>12</span></td>
        
    </tr>
    <tr>
        <td class="disabled"><span>13</span></td>
        <td><span>14</span></td>
        <td><span>15</span></td>
        <td><span>16</span></td>
        <td><span>17</span></td>
        <td><span>18</span></td>
        <td class="disabled"><span>19</span></td>
        
    </tr>
    <tr>
        <td class="disabled"><span>20</span></td>
        <td><span>21</span></td>
        <td><span>22</span></td>
        <td><span>23</span></td>
        <td><span>24</span></td>
        <td><span>25</span></td>
        <td class="disabled"><span>26</span></td>
        
    </tr>
    <tr>
        <td class="disabled"><span>27</span></td>
        <td class="disabled"><span>28</span></td>
        <td class="disabled"><span>29</span></td>
        <td class="disabled"><span>30</span></td>
        <td class="disabled"></td>
        <td class="disabled"></td>
        <td class="disabled"></td>
        
    </tr>
    
</table>
"""

pricing_tables = """
<div class="pricing-tables">
        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 (1pE)</td>
                <td id="valor_1_4_1p">$315</td>
            </tr>
            <tr>
                <td>Días 5-9 (1pE)</td>
                <td id="valor_5_9_1p">$302</td>
            </tr>
            <tr>
                <td>Días 10-14 (1pE)</td>
                <td id="valor_10_14_1p">$287</td>
            </tr>
            <tr>
                <td>Días 15-18 (1pE)</td>
                <td id="valor_15_18_1p">$287</td>
            </tr>
        </table>
        
        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 (2pE)</td>
                <td id="valor_1_4_2p">$285</td>
            </tr>
            <tr>
                <td>Días 5-9 (2pE)</td>
                <td id="valor_5_9_2p">$265</td>
            </tr>
            <tr>
                <td>Días 10-14 (2pE)</td>
                <td id="valor_10_14_2p">$251</td>
            </tr>
            <tr>
                <td>Días 15-18 (2pE)</td>
                <td id="valor_15_18_2p">$245</td>
            </tr>
        </table>

        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 (3pE)</td>
                <td id="valor_1_4_3p">$260</td>
            </tr>
            <tr>
                <td>Días 5-9 (3pE)</td>
                <td id="valor_5_9_3p">$253</td>
            </tr>
            <tr>
                <td>Días 10-14 (3pE)</td>
                <td id="valor_10_14_3p">$241</td>
            </tr>
            <tr>
                <td>Días 15-18 (3pE)</td>
                <td id="valor_15_18_3p">$234</td>
            </tr>
        </table>
    </div>
"""

pricing_tables_credit = """
<div class="pricing-tables-credit">
        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 (1pTC)</td>
                <td id="valor_1_4_1p">$305</td>
            </tr>
            <tr>
                <td>Días 5-9 (1pTC)</td>
                <td id="valor_5_9_1p">$288</td>
            </tr>
            <tr>
                <td>Días 10-14 (1pTC)</td>
                <td id="valor_10_14_1p">$280</td>
            </tr>
            <tr>
                <td>Días 15-18 (1pTC)</td>
                <td id="valor_15_18_1p">$276</td>
            </tr>
        </table>
        
        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 (2pTC)</td>
                <td id="valor_1_4_2p">$285</td>
            </tr>
            <tr>
                <td>Días 5-9 (2pTC)</td>
                <td id="valor_5_9_2p">$265</td>
            </tr>
            <tr>
                <td>Días 10-14 (2pTC)</td>
                <td id="valor_10_14_2p">$262</td>
            </tr>
            <tr>
                <td>Días 15-18 (2pTC)</td>
                <td id="valor_15_18_2p">$260</td>
            </tr>
        </table>

        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 (3pTC)</td>
                <td id="valor_1_4_3p">$260</td>
            </tr>
            <tr>
                <td>Días 5-9 (3pTC)</td>
                <td id="valor_5_9_3p">$253</td>
            </tr>
            <tr>
                <td>Días 10-14 (3pTC)</td>
                <td id="valor_10_14_3p">$251</td>
            </tr>
            <tr>
                <td>Días 15-18 (3pTC)</td>
                <td id="valor_15_18_3p">$249</td>
             </tr>
        </table>
    </div>
"""

pricing_tables_extra = """
    <div class="pricing-tables-extra">
        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 1erP (NoPA)</td>
                <td id="valor_1_4_1p_NoPA">$45</td>
            </tr>
            <tr>
                <td>Días 5-60 1erP (NoPA)</td>
                <td id="valor_5_60_1p_NoPA">$27</td>
            </tr>
        </table>
        
        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 1erP (SiPA)</td>
                <td id="valor_1_4_1p_SiPA">$50</td>
            </tr>
            <tr>
                <td>Días 5-60 1erP (SiPA)</td>
                <td id="valor_5_60_1p_SiPA">$30</td>
            </tr> 
        </table>

        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 PAdicional (NoPA)</td>
                <td id="valor_1_4_add_NoPA">$23</td>
            </tr>
            <tr>
                <td>Días 5-60 PAdicional (NoPA)</td>
                <td id="valor_5_60_add_NoPA">$14</td>
            </tr>
        </table>
        
        <table>
            <tr>
                <th>Días</th>
                <th>Valor</th>
            </tr>
            <tr>
                <td>Días 1-4 PAdicional (SiPA)</td>
                <td id="valor_1_4_add_SiPA">$25</td>
            </tr>
            <tr>
                <td>Días 5-60 PAdicional (SiPA)</td>
                <td id="valor_5_60_add_SiPA">$15</td>
            </tr>
        </table>
    </div>
"""
