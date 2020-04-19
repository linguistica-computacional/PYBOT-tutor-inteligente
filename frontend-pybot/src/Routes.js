import React from 'react';
import { Switch, Route } from 'react-router-dom';
import faq from './components/faq/faq';
import forum from './components/forum/forum';
import meetup from './components/meetup/meetup';
import reward from './components/reward/reward';
import projected from './components/statistics/projected';
import real from './components/statistics/real';
//import report-learning from './components/statistics/report-learning';
import start from './components/test-learning/start';
import Login from './components/user/login';
//import perfil-economic from './components/user/perfil-economic';
//import perfil-edit from './components/user/perfil-edit';
import register from './components/user/register';
import Dashboard from './Dashboard';


const Routes = () => {
	return(
			<Switch>
				<Route exact path='/' component={Dashboard} />				
				<Route path='/' component={Login} />
				
			</Switch>
		);
}

export default Routes;