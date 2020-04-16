import React from 'react';
import { Switch, Route } from 'react-router-dom';
import faq from './components/faq/faq';
import forum from './components/forum/forum';
import meetup from './components/meetup/meetup';
import reward from './components/reward/reward';
import projected from './components/statistics/projected';
import real from './components/statistics/real';
import report-learning from './components/statistics/report-learning';
import start from './components/test-learning/start';
import login from './components/user/login';
import perfil-economic from './components/user/perfil-economic';
import perfil-edit from './components/user/perfil-edit';
import register from './components/user/register';

const Router = () => {
	return(
			<Switch>
				<Route exact path='/' component={faq} />
				<Route exact path='/' component={forum} />
				<Route exact path='/' component={meetup} />
				<Route exact path='/' component={reward} />
				<Route exact path='/' component={projected} />
				<Route exact path='/' component={real} />
				<Route exact path='/' component={report-learning} />
				<Route exact path='/' component={start} />
				<Route exact path='/' component={login} />
				<Route exact path='/' component={perfil-economic} />
				<Route exact path='/' component={perfil-economic} />
				<Route exact path='/' component={register} />
			</Switch>
		);
}

export default Router;