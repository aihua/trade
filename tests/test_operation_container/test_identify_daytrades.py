from __future__ import absolute_import
import unittest

import trade as trade_tools


class TestTradeContainer_identify_daytrades_and_common_trades_case_00(
        unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=10,
                            price=2
                        )
        self.trade2 = trade_tools.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=-10,
                            price=3
                        )
        self.trade_container = trade_tools.OperationContainer(
            operations=[self.trade1,self.trade2])
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_two(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_10(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -10)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_0(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 0)

    def test_daytrades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.daytrades.keys()), 1)

    def test_check_daytrade_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].asset,
            self.asset
        )

    def test_daytrade_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].quantity,
            10
        )

    def test_daytrade_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].purchase.price,
            2
        )

    def test_daytrade_buy_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].purchase.quantity,
            10
        )

    def test_daytrade_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].sale.price,
            3
        )

    def test_daytrade_sale_quantity_should_be_minus_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].sale.quantity,
            -10
        )

    def test_daytrade_result_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].result,
            10
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_01(
        unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset('some asset')
        self.trade1 = trade_tools.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=10,
                            price=2
                        )
        self.trade2 = trade_tools.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=-5,
                            price=3
                        )
        self.trade_container = trade_tools.OperationContainer(
            operations=[self.trade1,self.trade2])
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_two(self):
        self.assertEqual(len(self.trade_container.operations), 2)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset].asset,
            self.asset
        )

    def test_common_trades1_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset].quantity,
            5
        )

    def test_common_trades1_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset].price,
            2
        )

    def test_daytrades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.daytrades.keys()), 1)

    def test_check_daytrade_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].asset,
            self.asset
        )

    def test_daytrade_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].quantity,
            5
        )

    def test_daytrade_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].purchase.price,
            2
        )

    def test_daytrade_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].purchase.quantity,
            5
        )

    def test_daytrade_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].sale.price,
            3
        )

    def test_daytrade_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].sale.quantity,
            -5
        )

    def test_daytrade_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset].result,
            5
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_02(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2,trade3])
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_three(self):
        self.assertEqual(len(self.trade_container.operations), 3)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 2)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].quantity,
            5
        )

    def test_common_trades0_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].price,
            2
        )

    def test_check_common_trades1_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].asset,
            self.asset2
        )

    def test_common_trades1_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].quantity,
            -5
        )

    def test_common_trades1_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset2].price,
            7
        )

    def test_daytrades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.daytrades.keys()), 1)

    def test_check_daytrade_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].asset,
            self.asset1
        )

    def test_daytrade_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].quantity,
            5
        )

    def test_daytrade_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.price,
            2
        )

    def test_daytrade_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.quantity,
            5
        )

    def test_daytrade_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.price,
            3
        )

    def test_daytrade_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.quantity,
            -5
        )

    def test_daytrade_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].result,
            5
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_03(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2,trade3,trade4])
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_four(self):
        self.assertEqual(len(self.trade_container.operations), 4)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].quantity,
            5
        )

    def test_common_trades0_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].price,
            2
        )

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.daytrades.keys()), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_04(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        trade5 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2,trade3,trade4,trade5])
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.operations), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_0(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 0)

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.daytrades.keys()), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].quantity,
            10
        )

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.quantity,
            10
        )

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.quantity,
            -10
        )

    def test_daytrade0_result_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].result,
            10
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_05(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=10
                )
        trade3 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        trade5 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=20
                )
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2,trade3,trade4,trade5])
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.operations), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_10(self):
        self.assertEqual(self.trade_container.operations[1].price, 10)

    def test_common_trades_len_should_be_0(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 0)

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(len(self.trade_container.daytrades.keys()), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].quantity,
            10
        )

    def test_daytrade0_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.quantity,
            10
        )

    def test_daytrade0_sale_price_should_be_15(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.price,
            15
        )

    def test_daytrade0_sale_quantity_should_be_minus_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.quantity,
            -10
        )

    def test_daytrade0_result_should_be_130(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].result,
            130
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_06(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        trade1 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        trade5 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=5,
                    price=4
                )
        self.trade_container = trade_tools.OperationContainer(
            operations=[trade1,trade2,trade3,trade4,trade5])
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.operations), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].quantity,
            10
        )

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].price,
            3
        )

    def test_daytrades_len_should_be_2(self):
        self.assertEqual(
            len(self.trade_container.daytrades.keys()),
            2
        )

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_07(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade_tools.Asset('some asset')
        self.asset2 = trade_tools.Asset('some other asset')
        self.asset3 = trade_tools.Asset('even other asset')
        trade1 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,price=10
                )
        trade5 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=5,
                    price=4
                )

        trade6 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=5,
                    price=4
                )
        trade7 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=-5,
                    price=2
                )

        trade8 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=5,
                    price=4
                )
        trade9 = trade_tools.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=-5,
                    price=4
                )

        self.trade_container = trade_tools.OperationContainer(
            operations=[
                trade1,trade2,trade3,trade4,trade5,trade6,trade7,trade8,trade9
            ]
        )
        self.trade_container.identify_daytrades_and_common_operations()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.trade_container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.trade_container.operations), 9)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.trade_container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.trade_container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.trade_container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.trade_container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 1)

    def test_check_common_trades0_asset(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].quantity,
            10
        )

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset1].price,
            3
        )

    def test_daytrades_len_should_be_3(self):
        self.assertEqual(
            len(self.trade_container.daytrades.keys()),
            3
        )

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].purchase.quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].sale.quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].purchase.quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].sale.quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset2].result,
            -15
        )

    def test_check_daytrade2_asset(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].asset,
            self.asset3
        )

    def test_daytrade2_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].quantity,
            10
        )

    def test_daytrade2_buy_price_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].purchase.price,
            4
        )

    def test_daytrade2_buy_quantity_should_be_10(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].purchase.quantity,
            10
        )

    def test_daytrade2_sale_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].sale.price,
            3
        )

    def test_daytrade2_sale_quantity_should_be_minus_5(self):
        self.assertEqual(
            self.trade_container.daytrades[self.asset3].sale.quantity,
            -10
        )
