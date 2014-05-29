import getPostcategoriestest as gp
import getPostIdstest as gp1
import getPostEntitiestest as gp2
import getXtest as X
import unittest
import trainpredicttest as tp

suite = unittest.TestLoader().loadTestsFromTestCase(gp.TestGetPostcategories)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(gp1.TestGetPostIds)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(gp2.TestGetPostEntities)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(X.TestGetX)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(tp.Testpredtrain)
unittest.TextTestRunner(verbosity=2).run(suite)
